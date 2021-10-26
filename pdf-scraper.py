import requests
import re
from bs4 import BeautifulSoup
from startup import Startup



startup_num = 5285

while startup_num <= 5287:
    # start and end bounds: 5285 to 5942
    url="https://angelmatch.io/pitch_decks/" + str(startup_num)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    startup_obj = Startup(startup_num)
    startup_name = Startup.get_name(startup_obj, soup)
    startup_amt = Startup.get_amount(startup_obj, soup)
    startup_link = Startup.get_pdflink(startup_obj, soup)


# output = "Name: {}\nAmount: {}\nLink: {}".format(startup_name, startup_amt, startup_link)
    output_to_write = "{},{},{},{}\n".format(startup_num, startup_name, startup_amt, startup_link)
# print(output_to_write)


    with open('output.txt', 'a') as f:
        # mode set to a. appends to existing
        f.write(output_to_write)
    
    startup_num += 1

f.close()

#extract pdf content with pymupdf
