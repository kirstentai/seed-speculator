import requests
import re
from bs4 import BeautifulSoup

class Startup:

    # def __init__(self, name, link_num, amount, pdf_link):
    def __init__(self, link_num):

        # self.name = name
        self.link_num = link_num
        # self.amount = amount
        # self.pdf_link = pdf_link


    def get_name(self, soup_link):
        for tag in soup_link.find_all('div', class_="card-header-title name"):
            name = tag.text.strip()
            return name
    

    def get_amount(self, soup_link):
        for tag in soup_link.find_all('div', class_="custom-filter first-left"):
            # custom-filter first-left -> box -> content -> field -> <p>
            p_finder = tag.find('p')

            if p_finder != None:
                amount_raised_string = p_finder.text.strip()
                amount = str(re.split(" ", amount_raised_string)[3])
                # return amount_raised_string #Amount raised:  $20M
                return amount

            return "No amount found."
    

    def get_pdflink(self, soup_link):
        for tag in soup_link.find_all('button'):
            # dl_link = tag.find('a', download_="")
            # all_buttons =  soup.find('button')
            airtable_link = tag.find(href=True)
            href_link = airtable_link['href']

            # note: implement if href is defined, download pdf else skip and raise warning in script
            if re.search(r"airtable", href_link):
                return href_link
            # else:
            #     return "No PDF link found."