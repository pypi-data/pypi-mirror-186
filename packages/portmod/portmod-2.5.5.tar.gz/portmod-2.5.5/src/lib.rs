#[macro_use]
extern crate serde_with;

mod dds;
mod error;
mod index;
mod metadata;
mod news;
mod yaml;

use crate::dds::get_dds_dimensions;
use crate::metadata::{
    CategoryMetadata, Group, GroupDeclaration, PackageMetadata, Person, Upstream,
};
use crate::news::News;
use crate::yaml::parse_yaml;
use digest::Digest;
use directories::{ProjectDirs, UserDirs};
use esplugin::{GameId, Plugin};
use fluent_bundle::types::FluentValue;
use fluent_templates::Loader;
use std::collections::HashMap;
use std::io::BufRead;
use std::io::BufReader;
use std::path::Path;
use unic_langid::LanguageIdentifier;

use pyo3::prelude::*;
use pyo3::types::{PyDict, PyFloat, PyLong};

use pyo3::exceptions::PyFileNotFoundError;
use pyo3::wrap_pyfunction;

#[cfg(debug_assertions)]
use fluent_templates::ArcLoader;

#[cfg(debug_assertions)]
fn debug_l10n_dir() -> String {
    let gil = Python::acquire_gil();
    let py = gil.python();
    fn get_dir(py: Python) -> PyResult<String> {
        let locale = PyModule::import(py, "portmodlib.l10n")?;
        locale.getattr("_DEBUG_L10N_DIR")?.extract()
    }
    let dir = get_dir(py).map_err(|e| {
        e.print_and_set_sys_last_vars(py);
    });
    if let Ok(dir) = dir {
        dir
    } else {
        panic!("Could not detect default encoding!");
    }
}

#[cfg(debug_assertions)]
thread_local!(static ARC_LOADER: ArcLoader = ArcLoader::builder(&debug_l10n_dir(), FALLBACK_LANG)
    .customize(|bundle| bundle.set_use_isolating(should_use_isolating()))
    .build()
    .unwrap());

fn should_use_isolating() -> bool {
    // Runtime cost of this should be minimal, but we might want to switch
    // to determining locale on the rust side of things.
    let gil = Python::acquire_gil();
    let py = gil.python();
    fn get_encoding(py: Python) -> PyResult<String> {
        let locale = PyModule::import(py, "locale")?;
        locale.getattr("getpreferredencoding")?.call0()?.extract()
    }
    let encoding = get_encoding(py).map_err(|e| {
        e.print_and_set_sys_last_vars(py);
    });
    if let Ok(encoding) = encoding {
        if encoding.starts_with("utf-") {
            return true;
        }
    } else {
        eprintln!("Could not detect default encoding!");
    }
    false
}

const FALLBACK_LANG: LanguageIdentifier = unic_langid::langid!("en-GB");

fluent_templates::static_loader! {
    static STATIC_LOADER = {
        locales: "./l10n",
        fallback_language: "en-GB",
        customise: |bundle| bundle.set_use_isolating(should_use_isolating()),
    };
}

#[allow(dead_code)]
#[allow(non_snake_case)]
fn main() {
    use pyo3::create_exception;
    use pyo3::prelude::*;

    #[pyfunction]
    pub fn parse_package_metadata(filename: &str) -> PyResult<PackageMetadata> {
        Ok(parse_yaml(filename)?)
    }

    #[pyfunction]
    pub fn parse_category_metadata(filename: &str) -> PyResult<CategoryMetadata> {
        Ok(parse_yaml(filename)?)
    }

    #[pyfunction]
    pub fn parse_yaml_dict(filename: &str) -> PyResult<HashMap<String, String>> {
        Ok(parse_yaml(filename)?)
    }

    #[pyfunction]
    pub fn parse_groups(filename: &str) -> PyResult<HashMap<String, GroupDeclaration>> {
        Ok(parse_yaml(filename)?)
    }

    #[pyfunction]
    pub fn parse_yaml_dict_dict(
        filename: &str,
    ) -> PyResult<HashMap<String, HashMap<String, String>>> {
        Ok(parse_yaml(filename)?)
    }

    #[pyfunction]
    pub fn parse_news(filename: &str) -> PyResult<News> {
        Ok(parse_yaml(filename)?)
    }

    #[pyfunction]
    fn get_masters(filename: &str) -> PyResult<Vec<String>> {
        let mut plugin = Plugin::new(GameId::Morrowind, Path::new(&filename));
        plugin
            .parse_file(true)
            .map_err(|x| crate::error::Error::Plugin(filename.to_string(), x))?;
        let list = plugin
            .masters()
            .map_err(|x| crate::error::Error::Plugin(filename.to_string(), x))?;
        Ok(list)
    }

    #[pyfunction]
    fn dds_dimensions(file: &str) -> PyResult<(u32, u32)> {
        let (width, height) = get_dds_dimensions(file)?;
        Ok((width, height))
    }

    #[pyfunction]
    fn l10n_lookup(lang: &str, text_id: &str, args: &PyDict) -> PyResult<String> {
        let lang_id: LanguageIdentifier = match lang.parse() {
            Ok(lang_id) => lang_id,
            Err(_) => {
                let gil = Python::acquire_gil();
                let py = gil.python();
                let log = py.import("warnings")?;
                log.getattr("warn")?.call(
                    (format!(
                        "User language identifier \"{}\" could not be parsed",
                        lang
                    ),),
                    None,
                )?;
                FALLBACK_LANG
            }
        };
        let args: Vec<PyResult<(String, FluentValue)>> = args
            .iter()
            .map(|(key, value)| {
                let typ = value.get_type();
                let key: String = key.extract()?;
                Ok(if typ.is_subclass_of::<PyLong>()? {
                    let value: i64 = value.extract()?;
                    (key, FluentValue::Number(value.into()))
                } else if typ.is_subclass_of::<PyFloat>()? {
                    let value: f64 = value.extract()?;
                    (key, FluentValue::Number(value.into()))
                } else {
                    (key, FluentValue::String(value.str()?.to_string().into()))
                })
            })
            .collect();
        for result in &args {
            if let Err(x) = result {
                let gil = Python::acquire_gil();
                let py = gil.python();
                return Err(x.clone_ref(py));
            }
        }
        let args: HashMap<String, FluentValue> = args.into_iter().map(|x| x.unwrap()).collect();
        #[cfg(debug_assertions)]
        return ARC_LOADER.with(|loader| Ok(loader.lookup_with_args(&lang_id, text_id, &args)));
        #[cfg(not(debug_assertions))]
        Ok(STATIC_LOADER.lookup_with_args(&lang_id, text_id, &args))
    }

    /// Hashes the given file
    /// 30MB appears to be a good buffer size for both large and small files
    #[pyfunction]
    fn _get_hash(filename: &str, funcs: Vec<&str>, buffer_size: usize) -> PyResult<Vec<String>> {
        let mut results: HashMap<&str, String> = HashMap::new();

        fn get_hash<T: Digest, R: std::io::Read>(
            hasher: T,
            reader: &mut BufReader<R>,
        ) -> PyResult<String>
        where
            T::OutputSize: std::ops::Add,
            <T::OutputSize as std::ops::Add>::Output: digest::generic_array::ArrayLength<u8>,
        {
            let mut hasher = hasher;
            loop {
                let buffer = reader.fill_buf()?;
                let size = buffer.len();
                if size == 0 {
                    break;
                }
                hasher.update(&buffer);
                reader.consume(size);
            }
            Ok(format!("{:x}", hasher.finalize()))
        }

        for func in &funcs {
            let file = std::fs::File::open(&filename)?;
            let mut reader = BufReader::with_capacity(buffer_size, file);
            match *func {
                "BLAKE3" => {
                    let mut hasher = blake3::Hasher::new();
                    loop {
                        let buffer = reader.fill_buf()?;
                        let size = buffer.len();
                        if size == 0 {
                            break;
                        }
                        if size > 128 * 1024 {
                            hasher.update_rayon(&buffer[0..size]);
                        } else {
                            hasher.update(buffer);
                        }
                        reader.consume(size);
                    }
                    results.insert("BLAKE3", format!("{}", hasher.finalize()));
                }
                "SHA512" => {
                    results.insert("SHA512", get_hash(sha2::Sha512::new(), &mut reader)?);
                }
                "SHA256" => {
                    results.insert("SHA256", get_hash(sha2::Sha256::new(), &mut reader)?);
                }
                "BLAKE2B" => {
                    results.insert("BLAKE2B", get_hash(blake2::Blake2b512::new(), &mut reader)?);
                }
                "MD5" => {
                    results.insert("MD5", get_hash(md5::Md5::new(), &mut reader)?);
                }
                _ => return Err(error::Error::UnsupportedHashType(func.to_string()).into()),
            }
        }

        Ok(funcs
            .iter()
            .map(|func| results.remove(func).unwrap())
            .collect())
    }

    #[pyfunction]
    fn update_index(index_path: &str, packages: Vec<index::PackageIndexData>) -> PyResult<()> {
        Ok(index::update_index(index_path, packages).map_err(error::Error::Tantivy)?)
    }

    #[pyfunction]
    /// Returns a json representation of the packages resulting from the query.
    fn query(
        index_path: &str,
        prefix: &str,
        query: &str,
        limit: usize,
    ) -> PyResult<Vec<index::PackageIndexData>> {
        Ok(index::query(index_path, prefix, query, limit).map_err(error::Error::Tantivy)?)
    }

    #[pymodule]
    /// A Python module implemented in Rust.
    fn portmod(py: Python, m: &PyModule) -> PyResult<()> {
        m.add_wrapped(wrap_pyfunction!(get_masters))?;
        m.add_wrapped(wrap_pyfunction!(dds_dimensions))?;
        m.add_wrapped(wrap_pyfunction!(parse_package_metadata))?;
        m.add_wrapped(wrap_pyfunction!(parse_category_metadata))?;
        m.add_wrapped(wrap_pyfunction!(parse_yaml_dict))?;
        m.add_wrapped(wrap_pyfunction!(parse_yaml_dict_dict))?;
        m.add_wrapped(wrap_pyfunction!(parse_groups))?;
        m.add_wrapped(wrap_pyfunction!(parse_news))?;
        m.add_wrapped(wrap_pyfunction!(l10n_lookup))?;
        m.add_wrapped(wrap_pyfunction!(_get_hash))?;
        m.add_wrapped(wrap_pyfunction!(update_index))?;
        m.add_wrapped(wrap_pyfunction!(query))?;
        m.add_class::<PackageMetadata>()?;
        m.add_class::<Upstream>()?;
        m.add_class::<CategoryMetadata>()?;
        m.add_class::<Group>()?;
        m.add_class::<Person>()?;
        m.add_class::<GroupDeclaration>()?;
        m.add_class::<News>()?;
        m.add_class::<index::PackageIndexData>()?;

        let submodule = PyModule::new(py, "directories")?;
        let user_dirs: UserDirs = UserDirs::new().ok_or_else(|| {
            PyErr::new::<PyFileNotFoundError, _>("No valid home directory path was found!")
        })?;
        let project_dirs: ProjectDirs =
            ProjectDirs::from("", "portmod", "portmod").ok_or_else(|| {
                PyErr::new::<PyFileNotFoundError, _>("No valid home directory path was found!")
            })?;

        submodule.add("download_dir", user_dirs.download_dir())?;
        submodule.add("cache_dir", project_dirs.cache_dir())?;
        submodule.add("data_dir", project_dirs.data_dir())?;
        submodule.add("config_dir", project_dirs.preference_dir())?;
        m.add_submodule(submodule)?;

        Ok(())
    }

    create_exception!(portmod, Error, pyo3::exceptions::PyException);
}
