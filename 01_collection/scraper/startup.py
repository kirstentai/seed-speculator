import requests
import re
from bs4 import BeautifulSoup

    
def get_name(start_num):
    url="https://angelmatch.io/pitch_decks/" + str(start_num)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for tag in soup.find_all('div', class_="card-header-title name"):
        name = tag.text.strip()
        return name


def get_amount(start_num):
    url="https://angelmatch.io/pitch_decks/" + str(start_num)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for tag in soup.find_all('div', class_="custom-filter first-left"):
        # custom-filter first-left -> box -> content -> field -> <p>
        p_finder = tag.find('p')

        if p_finder != None:
            amount_raised_string = p_finder.text.strip()
            amount = str(re.split(" ", amount_raised_string)[3])

            return amount

        return "No amount found."


def get_pdflink(start_num):
    url="https://angelmatch.io/pitch_decks/" + str(start_num)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for tag in soup.find_all('button'):
        # dl_link = tag.find('a', download_="")
        # all_buttons =  soup.find('button')
        airtable_link = tag.find(href=True)
        href_link = airtable_link['href']

        file_name = str(start_num) + ".pdf"


        # note: implement if href is defined, download pdf else skip and raise warning in script
        # try:
        if re.search(r"airtable", href_link):
        # print("regex: {}".format(href_link))
            response = requests.get(href_link)

            with open(file_name, 'wb') as f:
                f.write(response.content)
            return href_link
        # else:
        #     return "No PDF link found."

