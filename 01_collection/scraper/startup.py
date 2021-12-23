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
        # try:
        if re.search(r"airtable", href_link):
        # print("regex: {}".format(href_link))
            response = requests.get(href_link)

            with open(file_name, 'wb') as f:
                f.write(response.content)
            return href_link


def get_round(start_num):
    url="https://angelmatch.io/pitch_decks/" + str(start_num)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for tag in soup.find_all('div', class_="content"):
        link = tag.find(href=True)
        href_link = link['href']
        if re.search(r"by_stage", href_link):
            p_finder = tag.find('a')
            amount_raised_string = p_finder.text.strip()
            # print(amount_raised_string)

            return amount_raised_string


def get_industries(start_num):
    url="https://angelmatch.io/pitch_decks/" + str(start_num)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    industry_list = []
    for tag in soup.find_all('div', class_="content"):
        
        for href_elements in tag.find_all('a', href=True):
            href_link = href_elements['href']
            
            if re.search(r"by_category", href_link):
                industry_list.append(href_elements.text.strip())
    
    unique_set = set(industry_list)
    final_industry_list = list(unique_set)
    # print(f"list: {final_industry_list}")

    return final_industry_list
