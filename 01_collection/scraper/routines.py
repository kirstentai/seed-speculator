import requests
import sys
from bs4 import BeautifulSoup
from startup import get_name, get_amount, get_pdflink
from tqdm import *
import time    



# start and end bounds: 5285 to 5942 (657 items)
def main():

    start_num = 5285
    end_num = 5290
    nopdf_link = 0




    while start_num <= end_num:
        startup_name = get_name(start_num)
        startup_amt = get_amount(start_num)
        startup_link = get_pdflink(start_num)

        if startup_link == None:
            nopdf_link += 1
            print("No link: {}".format(nopdf_link))

        output = "Num: {}\nName: {}\nAmount: {}\nLink: {}".format(start_num, startup_name, startup_amt, startup_link)
        print(output)
        
        start_num += 1


# with tqdm(total=100, file=sys.stdout) as pbar:
#     for i in range(10):
#         main()
#         pbar.update(10)