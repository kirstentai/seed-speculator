# find pattern in url numbers

# find start and end bounds

#loop through each url from start to end -- get request

#beautifulsoup4 to pull out pdf link -- get airtable pdf link

# if href is defined, download pdf else skip and raise warning in script

#extract pdf content with pymupdf

# from requests_html import HTML
import requests
from bs4 import BeautifulSoup

url="https://angelmatch.io/pitch_decks/5286"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#pull out fund raised
for tag in soup.find_all('div', class_="content"):
    p_finder = tag.find('p')
    if p_finder != None:
        print(p_finder.text.strip())