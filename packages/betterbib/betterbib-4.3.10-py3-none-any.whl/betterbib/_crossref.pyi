import pybtex.database
from ._helpers import safeget as safeget
from ._tools import heuristic_unique_result as heuristic_unique_result, pybtex_to_dict as pybtex_to_dict
from ._warnings import UnsupportedBibTeXType as UnsupportedBibTeXType, UnsupportedCrossRefType as UnsupportedCrossRefType
from .errors import HttpError as HttpError, NotFoundError as NotFoundError
from _typeshed import Incomplete

__author_email__: str
__website__: str
BIBTEX_TO_CROSSREF_TYPEDICT: Incomplete
CROSSREF_TO_BIBTEX_TYPEDICT: Incomplete
CROSSREF_ADDITIONAL_SUPPORTED_TYPES: Incomplete

class Crossref:
    api_url: str
    def __init__(self) -> None: ...
    def get_by_doi(self, doi): ...
    def find_unique(self, entry: pybtex.database.Entry, minimum_score: float = ...) -> pybtex.database.Entry: ...
