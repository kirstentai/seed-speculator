# find pattern in url numbers

# find start and end bounds: 5285 to 5942

#loop through each url from start to end -- get request

#beautifulsoup4 to pull out pdf link -- get airtable pdf link


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

startup_obj = Startup(startup_num)
startup_name = Startup.get_name(startup_obj, soup)
startup_amt = Startup.get_amount(startup_obj, soup)
startup_link = Startup.get_pdflink(startup_obj, soup)

output = "Name: {}\nAmount: {}\nLink: {}".format(startup_name, startup_amt, startup_link)
output_to_write = "{},{},{}".format(startup_name, startup_amt, startup_link)
print(output_to_write)

with open('output.txt', 'w') as f:
    f.write(output_to_write)
    f.close()