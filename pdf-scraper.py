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
from startup import Startup

startup_num = 5285
url="https://angelmatch.io/pitch_decks/" + str(startup_num)
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

startup_5285 = Startup(startup_num)
name_5285 = Startup.get_name(startup_5285, soup)
amt_5285 = Startup.get_amount(startup_5285, soup)
# print("startup name: ", name_5285)

#pull out fund raised
# for tag in soup.find_all('div', class_="custom-filter first-left"):
#     # custom-filter first-left -> box -> content -> field -> <p>
#     p_finder = tag.find('p')

#     if p_finder != None:
#         amount_raised = p_finder.text.strip()
        # print(amount_raised)

# airtable pdf link
for tag in soup.find_all('button'):
    # dl_link = tag.find('a', download_="")
    # all_buttons =  soup.find('button')
    airtable_link = tag.find(href=True)
    href_link = airtable_link['href']
    if re.search(r"airtable", href_link):
        pass
        # print(href_link)

    # print("A tag: ",airtable_link)
    # print("Airtable: ",airtable_link['href'])



output = "Name: {}\n{}\nLink: --".format(name_5285, amt_5285)
print(output)

# with open('output.txt', 'w') as f:
#     f.write(output)
#     f.close()