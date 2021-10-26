# find pattern in url numbers

# find start and end bounds: 5285 to 5942

#loop through each url from start to end -- get request

#beautifulsoup4 to pull out pdf link -- get airtable pdf link

# if href is defined, download pdf else skip and raise warning in script

#extract pdf content with pymupdf

# from requests_html import HTML
import requests
import re
from bs4 import BeautifulSoup

startup_num = 5285
url="https://angelmatch.io/pitch_decks/" + str(startup_num)
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# extract startup name
for tag in soup.find_all('div', class_="card-header-title name"):
    print("Name: ",tag.text.strip())

#pull out fund raised
for tag in soup.find_all('div', class_="custom-filter first-left"):
    # custom-filter first-left -> box -> content -> field -> <p>
    p_finder = tag.find('p')

    if p_finder != None:
        print(p_finder.text.strip())

# airtable pdf link
for tag in soup.find_all('button'):
    # dl_link = tag.find('a', download_="")
    # all_buttons =  soup.find('button')
    airtable_link = tag.find(href=True)
    href_link = airtable_link['href']
    if re.search(r"airtable", href_link):
        print(href_link)

    # print("A tag: ",airtable_link)
    # print("Airtable: ",airtable_link['href'])
