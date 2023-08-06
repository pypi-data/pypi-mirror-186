// Copyright 2019-2020 Portmod Authors
// Distributed under the terms of the GNU General Public License v3

use crate::error::Error;
use pyo3::prelude::*;
use serde::de::{self, MapAccess, Visitor};
use serde::{Deserialize, Deserializer, Serialize};
use std::fmt;
use std::str::FromStr;

#[pyclass(module = "portmodlib.portmod")]
#[skip_serializing_none]
#[derive(Clone, Debug, PartialEq, Serialize)]
/// An individual maintainer
/// Either name or email is required.
pub struct Person {
    #[pyo3(get, set)]
    /// Maintainer's Name or Pseudonym
    name: Option<String>,
    #[pyo3(get, set)]
    /// Maintainer's Email
    email: Option<String>,
    #[pyo3(get, set)]
    /// Description. Can be used to describe the status of maintainership
    desc: Option<String>,
}

impl fmt::Display for Person {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match (&self.name, &self.email) {
            (Some(name), Some(email)) => write!(f, "{} <{}>", name, email),
            (Some(name), None) => write!(f, "{}", name),
            (None, Some(email)) => write!(f, "{}", email),
            (None, None) => write!(f, ""),
        }
    }
}

#[pymethods]
impl Person {
    fn __str__(&self) -> PyResult<String> {
        Ok(format!("{}", self))
    }
}

impl FromStr for Person {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        // FIXME: This treats < and > equally and allows the omission of the closing bracket
        let tokens: Vec<&str> = s.split(|c: char| c == '<' || c == '>').collect();
        Ok(Person {
            email: tokens.get(1).map(|x| x.trim().to_string()),
            name: Some(tokens[0].trim().to_string()),
            desc: None,
        })
    }
}

#[derive(Debug, Deserialize)]
pub struct PersonAux {
    email: Option<String>,
    name: Option<String>,
    desc: Option<String>,
}

// FIXME: This is messy and I'd rather not do it manually.
// If possible, it should be replaced with a simpler derive in future
struct PersonVisitor;

impl<'de> Visitor<'de> for PersonVisitor {
    type Value = Person;

    fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
        formatter.write_str("string or map")
    }

    fn visit_str<E>(self, value: &str) -> Result<Person, E>
    where
        E: de::Error,
    {
        Ok(FromStr::from_str(value).unwrap())
    }

    fn visit_map<M>(self, map: M) -> Result<Person, M::Error>
    where
        M: MapAccess<'de>,
    {
        let aux: PersonAux = Deserialize::deserialize(de::value::MapAccessDeserializer::new(map))?;
        Ok(Person {
            name: aux.name,
            desc: aux.desc,
            email: aux.email,
        })
    }
}

impl<'de> Deserialize<'de> for Person {
    fn deserialize<D>(deserializer: D) -> Result<Person, D::Error>
    where
        D: Deserializer<'de>,
    {
        deserializer.deserialize_any(PersonVisitor)
    }
}
