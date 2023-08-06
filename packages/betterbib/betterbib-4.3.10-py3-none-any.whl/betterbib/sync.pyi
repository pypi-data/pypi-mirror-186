from . import errors as errors
from ._crossref import Crossref as Crossref
from ._dblp import Dblp as Dblp
from ._retractions import check_retractions as check_retractions
from .journal_abbrev import journal_abbrev as journal_abbrev
from pybtex.database import Entry as Entry

def sync(d: dict[str, Entry], source: str, long_journal_names: bool, max_workers: int, verbose: bool, minimum_score: float) -> dict[str, Entry]: ...
