from scraper.startup import *
from scraper.io import *




def main():
    """ start and end bounds: 5285 to 5942 (657 items)"""
    
    start_num = 5285
    end_num = 5942
    master_dict = {}
    # master_list = []

    while start_num <= end_num:
        startup_name = get_name(start_num)
        startup_amt = get_amount(start_num)
        # startup_link = get_pdflink(start_num)
        startup_round = get_round(start_num)
        industries_list = get_industries(start_num)

        # if startup_link == None:
        #     nopdf_link += 1
        #     print("No link: {}".format(nopdf_link))

        output = "Num: {} | Name: {} | Amount: {} | Round: {} | Industries: {}".format(start_num, startup_name, startup_amt,
                                                                                        startup_round, industries_list)
        print(output)
        # output_dict = output_results(master_dict, start_num, startup_amt, startup_round, industries_list)
        output_results(master_dict, start_num, startup_amt, startup_round, industries_list)
        # print(output_dict)
        # master_list.append(output_dict)
        
        write_results("output.json", master_dict)
        start_num += 1


def output_results(startup_dict, startup_no, startup_amt, startup_round, industries_list):

    startup_dict[startup_no] = {}
    startup_dict[startup_no]['amount'] = startup_amt
    startup_dict[startup_no]['round'] = startup_round
    startup_dict[startup_no]['industries'] = industries_list
    
    return startup_dict