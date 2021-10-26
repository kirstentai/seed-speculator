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
                amount_raised = p_finder.text.strip()
                return amount_raised

            return "No amount found."
    