import scraper
import requests
from bs4 import BeautifulSoup
from scraper.startup import Startup

def test_name_retrieves_correct_result():
    url = "https://angelmatch.io/pitch_decks/5808"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    name = Startup(5808).get_name(soup)
    assert name == "Slidebean"