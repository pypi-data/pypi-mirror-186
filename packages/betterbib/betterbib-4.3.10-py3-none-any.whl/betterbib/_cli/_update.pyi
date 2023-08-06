from .._tools import bibtex_parser as bibtex_parser, convert_to_latex as convert_to_latex, dict_to_string as dict_to_string, preserve_title_capitalization as preserve_title_capitalization, remove_multiple_spaces as remove_multiple_spaces, set_page_range_separator as set_page_range_separator, write as write
from ..adapt_doi_urls import adapt_doi_urls as adapt_doi_urls
from ..journal_abbrev import journal_abbrev as journal_abbrev
from ..sync import sync as sync
from .helpers import add_file_parser_arguments as add_file_parser_arguments, add_formatting_parser_arguments as add_formatting_parser_arguments

def run(args) -> None: ...
def add_args(parser): ...
