import pytest
from extract.extract_meta import *

def test_results_write_json():
    ...

def test_capture_text():
    filepath = get_filepath(5289)
    assert filepath == '/Users/kirstent/Downloads/career/technical-portfolio/seed_speculator/02_extraction/5289'



@pytest.mark.skip
def test_capture_text():
    extract_text_page(filepath, page_number)
