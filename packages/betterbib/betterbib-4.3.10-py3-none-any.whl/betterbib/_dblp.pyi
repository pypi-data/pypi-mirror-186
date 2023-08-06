from ._tools import heuristic_unique_result as heuristic_unique_result, pybtex_to_dict as pybtex_to_dict
from .errors import HttpError as HttpError, NotFoundError as NotFoundError

class Dblp:
    api_url: str
    def __init__(self) -> None: ...
    def find_unique(self, entry, minimum_score: float = ...): ...
