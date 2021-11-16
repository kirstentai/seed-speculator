from startup import get_name, get_amount, get_pdflink
# from tqdm import *
# import time    



def main():
    """ start and end bounds: 5285 to 5942 (657 items)"""
    
    start_num = 5285
    end_num = 5942
    nopdf_link = 0


    while start_num <= end_num:
        startup_name = get_name(start_num)
        startup_amt = get_amount(start_num)
        startup_link = get_pdflink(start_num)

        if startup_link == None:
            nopdf_link += 1
            print("No link: {}".format(nopdf_link))

        output = "Num: {} | Name: {} | Amount: {} | Link: {}".format(start_num, startup_name, startup_amt, startup_link)
        print(output)
        
        start_num += 1
        # time.sleep(0.001)

# for i in tqdm(range(20)):
#     main()
#     time.sleep(0.001)
main()