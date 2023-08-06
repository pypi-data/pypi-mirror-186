// Copyright 2019-2020 Portmod Authors
// Distributed under the terms of the GNU General Public License v3

use pyo3::prelude::*;
use serde::{Deserialize, Serialize};

#[pyclass]
#[skip_serializing_none]
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct News {
    #[pyo3(get, set)]
    #[serde(rename = "Title")]
    /// A short descriptive title
    pub title: String,
    #[pyo3(get, set)]
    #[serde(rename = "Author")]
    // FIXME: Allow this field to be a list so that multiple authors can be specified
    /// Author's name and email address, in the form Real Name <email@address>
    pub author: String,
    #[pyo3(get, set)]
    #[serde(rename = "Translator")]
    // FIXME: Allow this field to be a list so that multiple authors can be specified
    /// Translator's name and email address, in the form Real Name <email@address>
    pub translator: Option<String>,
    #[pyo3(get, set)]
    #[serde(rename = "Posted")]
    /// Date of posting, in yyyy-mm-dd format
    pub posted: String,
    #[pyo3(get, set)]
    #[serde(rename = "Revision")]
    pub revision: String,
    #[pyo3(get, set)]
    #[serde(rename = "News-Item-Format")]
    /// Only supported format is 2.0
    pub news_item_format: String,
    #[pyo3(get, set)]
    #[serde(rename = "Body")]
    /// Contents of the news article
    pub body: String,
    #[pyo3(get, set)]
    #[serde(rename = "Display-If-Installed")]
    /// Required installed packages for the news to be displayed
    pub display_if_installed: Option<String>,
    #[pyo3(get, set)]
    #[serde(rename = "Display-If-Keyword")]
    /// Required keywords for the news to be displayed
    pub display_if_keyword: Option<String>,
    #[pyo3(get, set)]
    #[serde(rename = "Display-If-Profile")]
    /// Required profiles for the news to be displayed
    pub display_if_profile: Option<String>,
}
