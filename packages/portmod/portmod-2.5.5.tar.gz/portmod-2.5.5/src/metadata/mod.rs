// Copyright 2019-2020 Portmod Authors
// Distributed under the terms of the GNU General Public License v3

pub use crate::metadata::person::Person;
use derive_more::Display;
use pyo3::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::{HashMap, HashSet};

mod person;

#[pyclass]
#[skip_serializing_none]
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct CategoryMetadata {
    /// Description of the category.
    #[pyo3(get, set)]
    pub longdescription: String,
    /// Maintainer, or list of maintainers for the category
    pub maintainer: Option<Maintainers>,
}

#[pyclass(module = "portmodlib.portmod")]
#[skip_serializing_none]
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct Upstream {
    /// maintainers/authors of the original mod.
    pub maintainer: Option<Maintainers>,
    /// URL where a changelog for the mod can be found. Must be version independent
    #[pyo3(get, set)]
    pub changelog: Option<String>,
    /// URL where the location of the upstream documentation can be found.
    /// The link must not point to any third party documentation and must be version independent
    #[pyo3(get, set)]
    pub doc: Option<String>,
    /// A place where bugs can be reported in the form of an URL or an e-mail address prefixed with mailto:
    #[serde(rename = "bugs-to")]
    #[pyo3(get, set)]
    pub bugs_to: Option<String>,
}

#[pymethods]
impl Upstream {
    #[getter(maintainer)]
    fn maintainer(&self) -> PyObject {
        match &self.maintainer {
            Some(maintainer) => maintainer.clone().into(),
            None => {
                let gil = Python::acquire_gil();
                let py = gil.python();
                py.None()
            }
        }
    }
}

#[pyclass(module = "portmodlib.portmod")]
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize, Display)]
#[display(fmt = "{} group", group)]
pub struct Group {
    #[pyo3(get, set)]
    group: String,
}

#[pymethods]
impl Group {
    fn __str__(&self) -> PyResult<String> {
        Ok(format!("{}", self))
    }
}

#[pyclass(module = "portmodlib.portmod")]
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct GroupDeclaration {
    #[pyo3(get, set)]
    desc: String,
    #[pyo3(get, set)]
    // FIXME: use Maintainer instead of Person to allow heirarchical groups
    // Requires better py03 support for enums
    // See https://github.com/PyO3/pyo3/issues/417
    members: Vec<Person>,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(untagged)]
pub enum Maintainer {
    Group(Group),
    // Note: since all person fields are technically optional, this needs to be second so that
    // groups aren't just considered to be empty Person objects with an unexpected 'group' field
    Person(Person),
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(untagged)]
pub enum Maintainers {
    Single(Maintainer),
    Multiple(Vec<Maintainer>),
}

impl From<Maintainers> for PyObject {
    fn from(maintainers: Maintainers) -> PyObject {
        let gil = Python::acquire_gil();
        let py = gil.python();
        match maintainers {
            Maintainers::Single(ref maintainer) => get_maintainer(maintainer),
            Maintainers::Multiple(ref maintainers) => {
                let maintainer_list: Vec<PyObject> =
                    maintainers.iter().map(get_maintainer).collect();
                IntoPy::into_py(maintainer_list, py)
            }
        }
    }
}

#[pyclass(module = "portmodlib.portmod")]
#[skip_serializing_none]
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PackageMetadata {
    /// Description of the package
    #[pyo3(get, set)]
    pub longdescription: Option<String>,
    /// Maintainer, or list of maintainers for the package
    pub maintainer: Option<Maintainers>,
    #[serde(rename = "use")]
    /// Use flags and their descriptions. Key is the flag name, value is the description
    #[pyo3(get, set)]
    #[serde(skip_serializing_if = "HashMap::is_empty")]
    #[serde(default)]
    pub r#use: HashMap<String, String>,
    /// Description of the package's upstream information.
    #[pyo3(get, set)]
    pub upstream: Option<Upstream>,
    #[pyo3(get, set)]
    #[serde(default, skip_serializing_if = "HashSet::is_empty")]
    /// Tags for searching
    pub tags: HashSet<String>,
}

fn get_maintainer(maintainer: &Maintainer) -> PyObject {
    let gil = Python::acquire_gil();
    let py = gil.python();
    match maintainer {
        Maintainer::Person(person) => IntoPy::into_py(person.clone(), py),
        Maintainer::Group(group) => IntoPy::into_py(group.clone(), py),
    }
}

#[pymethods]
impl PackageMetadata {
    #[getter(maintainer)]
    fn maintainer(&self) -> PyObject {
        match &self.maintainer {
            Some(maintainer) => maintainer.clone().into(),
            None => {
                let gil = Python::acquire_gil();
                let py = gil.python();
                py.None()
            }
        }
    }
}
