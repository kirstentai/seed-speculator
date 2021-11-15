from scraper.startup import *

def test_name_retrieves_correct_result():

    startup_number = 5808
    name = get_name(startup_number)
    
    assert name == "Slidebean"


def test_amount_correct():

    startup_number = 5808
    name = get_amount(startup_number)
    
    assert name == "$35K"


def test_download_pdf():

    startup_number = 5808
    name = get_pdflink(startup_number)
    assert name == "https://dl.airtable.com/.attachments/7189370fb80c32038cc68615c96e0967/4a550db6/slidebeandeck.pdf"