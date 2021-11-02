import requests
from bs4 import BeautifulSoup
from scraper.startup import Startup
from tqdm import tqdm

from scraper.io import write_results

def main():
    init_num = 5801
    start_num = 5801
    end_num = 5942
    nopdf_link = 0

    results = []

    while start_num <= end_num:
        # start and end bounds: 5285 to 5942 (657 items)
        url="https://angelmatch.io/pitch_decks/" + str(start_num)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        startup_obj = Startup(start_num)
        startup_name = Startup.get_name(startup_obj, soup)
        startup_amt = Startup.get_amount(startup_obj, soup)
        startup_link = Startup.get_pdflink(startup_obj, soup)

        if startup_link == None:
            nopdf_link += 1

        # output = "Name: {}\nAmount: {}\nLink: {}".format(startup_name, startup_amt, startup_link)
        # print(output)

        results.append({"start_num": start_num, "startup_name":startup_name, "startup_amt": startup_amt, "startup_link": startup_link})

        # output_to_write = "{},{},{},{}\n".format(start_num, startup_name, startup_amt, startup_link)
        # # print(output_to_write)

        # #Testing items properly stored
        # # print("test objs: name-{},amt-{},link-{}".format(startup_obj.name, startup_obj.amount, startup_obj.pdf_link))

        # with open('output.txt', 'a') as parsed_file:
        # #     # mode set to a. appends to existing
        #     parsed_file.write(output_to_write)
        
        # start_num += 1
    
    write_results(results)

    with open('tracker.txt', 'a') as track_file:
        output = "\n{} to {}: {} items with no link.".format(init_num, end_num, nopdf_link)
        print(output)
        track_file.write(output)

    track_file.close()
    parsed_file.close()

    #extract pdf content with pymupdf
