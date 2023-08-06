# Copyright 2019-2020 Portmod Authors
# Distributed under the terms of the GNU General Public License v3

"""Type hints for Native Rust Extension"""
from typing import Any, Dict, List, Optional, Set, Union

# Ideally this file could eventually be generated automatically
# See https://github.com/PyO3/pyo3/issues/510

class Group:
    group: str

class Person:
    """
    An individual maintainer
    Either name or email is required.
    """

    # Maintainer's Name or Pseudonym
    name: Optional[str]
    # Maintainer's Email
    email: Optional[str]
    # Description. Can be used to describe the status of maintainership
    desc: Optional[str]

class GroupDeclaration:
    desc: str
    members: List[Person]

Maintainer = Union[Group, Person]
Maintainers = Union[Maintainer, List[Maintainer]]

class Upstream:
    # maintainers/authors of the original mod.
    maintainer: Optional[Maintainers]
    # URL where a changelog for the mod can be found. Must be version independent
    changelog: Optional[str]
    # URL where the location of the upstream documentation can be found.
    # The link must not point to any third party documentation and must be version independent
    doc: Optional[str]
    # A place where bugs can be reported in the form of an URL or an e-mail address prefixed with mailto:
    bugs_to: Optional[str]

class PackageMetadata:
    # Description of the package
    longdescription: Optional[str]
    # Maintainer, or list of maintainers for the package
    maintainer: Optional[Maintainers]
    # Use flags and their descriptions. Key is the flag name, value is the description
    use: Dict[str, str]
    # Tags for searching
    tags: Set[str]
    # Description of the package's upstream information.
    upstream: Optional[Upstream]

class CategoryMetadata:
    # Description of the category.
    longdescription: str
    # Maintainer, or list of maintainers for the category
    maintainer: Optional[Maintainers]

class News:
    # A short descriptive title
    title: str
    # Author's name and email address, in the form Real Name <email@address>
    author: str
    # Translator's name and email address, in the form Real Name <email@address>
    translator: Optional[str]
    # Date of posting, in yyyy-mm-dd format
    posted: str
    revision: str
    # Only supported format is 2.0
    news_item_format: str
    # Contents of the news article
    body: str
    # Required installed packages for the news to be displayed
    display_if_installed: Optional[str]
    # Required keywords for the news to be displayed
    display_if_keyword: Optional[str]
    # Required profiles for the news to be displayed
    display_if_profile: Optional[str]

def l10n_lookup(locale: str, msg_id: str, kwargs: Dict[str, Any]) -> str: ...
def get_masters(filename: str) -> List[str]: ...
def parse_yaml_dict(filename: str) -> Dict[str, str]: ...
def parse_yaml_dict_dict(filename: str) -> Dict[str, Dict[str, str]]: ...
def parse_news(filename: str) -> News: ...
def parse_groups(filename: str) -> Dict[str, GroupDeclaration]: ...
def parse_category_metadata(filename: str) -> CategoryMetadata: ...
def parse_package_metadata(filename: str) -> PackageMetadata: ...
def _get_hash(filename: str, algs: List[str], buffer_size: int) -> List[str]: ...

class PackageIndexData:
    """Data class for package metadata returned by query results"""

    cpn: str
    prefix: str
    category: str
    package: str
    name: str
    desc: str
    homepage: Optional[str]
    other_homepages: List[str]
    license: Optional[str]
    longdescription: Optional[str]
    maintainers: List[str]
    upstream_maintainers: List[str]
    upstream_doc: Optional[str]
    upstream_bugs_to: Optional[str]
    upstream_changelog: Optional[str]
    tags: Set[str]

    def __init__(
        self, cpn: str, prefix: str, category: str, package: str, name: str, desc: str
    ): ...

def update_index(index_path: str, packages: List[PackageIndexData]): ...
def query(
    index_path: str, prefix: str, query: str, limit: int
) -> List[PackageIndexData]: ...

class _Directories:
    cache_dir: str
    download_dir: Optional[str]
    config_dir: str
    data_dir: str

directories: _Directories
