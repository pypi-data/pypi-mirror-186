use pyo3::prelude::*;
use serde::de;
use std::collections::HashSet;
use tantivy::collector::{Count, TopDocs};
use tantivy::directory::MmapDirectory;
use tantivy::schema::{IndexRecordOption, Schema, Term, STORED, STRING, TEXT};
use tantivy::{
    doc,
    query::{BooleanQuery, Query, QueryParser, TermQuery},
    Index,
};

/// Deserializes a vector containing a single string as a string
/// Tantivy stores all data as lists internally,
/// so we unwrap the string for single-element fields
/// These fields are expected to always be present
fn deserialize_vec_string<'de, D>(deserializer: D) -> Result<String, D::Error>
where
    D: de::Deserializer<'de>,
{
    struct VecStringVisitor;

    impl<'de> de::Visitor<'de> for VecStringVisitor {
        type Value = String;

        fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
            formatter.write_str("a vector containing a single string")
        }

        fn visit_seq<V>(self, mut visitor: V) -> Result<Self::Value, V::Error>
        where
            V: de::SeqAccess<'de>,
        {
            visitor.next_element().map(|x| x.unwrap())
        }
    }

    deserializer.deserialize_any(VecStringVisitor)
}

/// Deserializes a vector containing a single string as an optional String
/// Tantivy stores all data as lists internally,
/// so we unwrap the string for single-element fields
fn deserialize_vec_option<'de, D>(deserializer: D) -> Result<Option<String>, D::Error>
where
    D: de::Deserializer<'de>,
{
    struct VecOptionVisitor;

    impl<'de> de::Visitor<'de> for VecOptionVisitor {
        type Value = Option<String>;

        fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
            formatter.write_str("a vector containing a single string")
        }

        fn visit_seq<V>(self, mut visitor: V) -> Result<Self::Value, V::Error>
        where
            V: de::SeqAccess<'de>,
        {
            visitor.next_element()
        }
    }

    deserializer.deserialize_any(VecOptionVisitor)
}

/// Data class for package metadata returned by query results
#[pyclass(module = "portmodlib.portmod")]
#[derive(Clone, Default, Debug, PartialEq, Deserialize)]
pub struct PackageIndexData {
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_string")]
    pub cpn: String,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_string")]
    pub prefix: String,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_string")]
    pub category: String,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_string")]
    pub package: String,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_string")]
    pub name: String,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_string")]
    pub desc: String,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_option", default)]
    pub homepage: Option<String>,
    #[pyo3(get, set)]
    #[serde(default)]
    pub other_homepages: Vec<String>,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_option", default)]
    pub license: Option<String>,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_option", default)]
    pub longdescription: Option<String>,
    #[pyo3(get, set)]
    #[serde(default)]
    pub maintainers: Vec<String>,
    #[pyo3(get, set)]
    #[serde(default)]
    pub upstream_maintainers: Vec<String>,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_option", default)]
    pub upstream_doc: Option<String>,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_option", default)]
    pub upstream_bugs_to: Option<String>,
    #[pyo3(get, set)]
    #[serde(deserialize_with = "deserialize_vec_option", default)]
    pub upstream_changelog: Option<String>,
    #[pyo3(get, set)]
    #[serde(default)]
    pub tags: HashSet<String>,
}

#[pymethods]
impl PackageIndexData {
    #[new]
    pub fn new(
        cpn: String,
        prefix: String,
        category: String,
        package: String,
        name: String,
        desc: String,
    ) -> Self {
        PackageIndexData {
            cpn,
            prefix,
            category,
            package,
            name,
            desc,
            ..Default::default()
        }
    }
}

pub fn update_index(index_path: &str, packages: Vec<PackageIndexData>) -> tantivy::Result<()> {
    let mut schema_builder = Schema::builder();
    let prefix = schema_builder.add_text_field("prefix", STRING | STORED);
    let cpn = schema_builder.add_text_field("cpn", STRING | STORED);
    let category = schema_builder.add_text_field("category", TEXT | STORED);
    let package_name = schema_builder.add_text_field("package", TEXT | STORED);
    let name = schema_builder.add_text_field("name", TEXT | STORED);
    let desc = schema_builder.add_text_field("desc", TEXT | STORED);
    let longdescription = schema_builder.add_text_field("longdescription", TEXT | STORED);
    let homepage = schema_builder.add_text_field("homepage", STRING | STORED);
    let other_homepages = schema_builder.add_text_field("other_homepages", STORED);
    let license = schema_builder.add_text_field("license", TEXT | STORED);
    let maintainers = schema_builder.add_text_field("maintainers", TEXT | STORED);
    let upstream_maintainers = schema_builder.add_text_field("upstream_maintainers", TEXT | STORED);
    let upstream_doc = schema_builder.add_text_field("upstream_doc", STRING | STORED);
    let upstream_bugs_to = schema_builder.add_text_field("upstream_bugs_to", STRING | STORED);
    let upstream_changelog = schema_builder.add_text_field("upstream_changelog", STRING | STORED);
    let tags = schema_builder.add_text_field("tags", TEXT | STORED);
    let schema = schema_builder.build();

    let index = Index::open_or_create(MmapDirectory::open(index_path)?, schema)?;
    let mut index_writer = index.writer(100_000_000)?;

    for package in packages {
        let mut document = doc!(
            prefix => package.prefix,
            cpn => package.cpn,
            category => package.category,
            package_name => package.package,
            name => package.name,
            desc => package.desc,
        );
        if let Some(value) = package.longdescription {
            document.add_text(longdescription, value);
        }
        if let Some(value) = package.homepage {
            document.add_text(homepage, value);
        }
        for other_homepage in package.other_homepages {
            document.add_text(other_homepages, other_homepage);
        }
        if let Some(value) = package.license {
            document.add_text(license, value);
        }
        for maintainer in package.maintainers {
            document.add_text(maintainers, maintainer);
        }
        for maintainer in package.upstream_maintainers {
            document.add_text(upstream_maintainers, maintainer);
        }
        if let Some(value) = package.upstream_doc {
            document.add_text(upstream_doc, value);
        }
        if let Some(value) = package.upstream_bugs_to {
            document.add_text(upstream_bugs_to, value);
        }
        if let Some(value) = package.upstream_changelog {
            document.add_text(upstream_changelog, value);
        }
        for tag in package.tags {
            document.add_text(tags, tag);
        }
        index_writer.add_document(document)?;
    }

    index_writer.commit()?;
    Ok(())
}

/// Returns a json representation of the packages resulting from the query.
pub fn query(
    index_path: &str,
    prefix: &str,
    query: &str,
    limit: usize,
) -> tantivy::Result<Vec<PackageIndexData>> {
    let index = Index::open(MmapDirectory::open(index_path)?)?;
    let searcher = index.reader()?.searcher();
    let schema = index.schema();

    let query_parser = QueryParser::for_index(
        &index,
        vec![
            schema.get_field("category").unwrap(),
            schema.get_field("package").unwrap(),
            schema.get_field("name").unwrap(),
            schema.get_field("desc").unwrap(),
            schema.get_field("longdescription").unwrap(),
            schema.get_field("tags").unwrap(),
        ],
    );
    let prefix_term_query: Box<dyn Query> = Box::new(TermQuery::new(
        Term::from_field_text(schema.get_field("prefix").unwrap(), prefix),
        IndexRecordOption::Basic,
    ));
    let query = query_parser.parse_query(query)?;
    let query = BooleanQuery::intersection(vec![query, prefix_term_query]);
    let (top_docs, _) = searcher.search(&query, &(TopDocs::with_limit(limit), Count))?;

    let mut results = vec![];

    for (_, doc_address) in top_docs {
        let doc = &searcher.doc(doc_address)?;
        let package_data: PackageIndexData = serde_json::from_str(&schema.to_json(doc))?;
        results.push(package_data);
    }
    Ok(results)
}
