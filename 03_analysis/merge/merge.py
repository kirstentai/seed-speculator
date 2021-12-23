""" Merges dictionaries from 2 scraping events"""
import json


def main():
    # read in json files
    file_name_basic = 'output_01.json'
    file_name_attributes = 'output_02.json'

    f_1 = open(file_name_basic)
    data_1 = json.load(f_1)

    f_2 = open(file_name_attributes)
    data_2 = json.load(f_2)
    
    # merging 2 dictionaries
    merged_list = list_merged_dict(data_1, data_2)
    print(merged_list)
    json_dict = {"startup_info": merged_list}
    # print(f"json dict: {json_dict}")
    f_1.close()
    f_2.close()

    # output to consolidated file
    filename = 'output_final.json'
    write_results(filename, json_dict)


def list_merged_dict(json_data, json_data_2):
    """ Returns a list of transformed dictionaries"""
    master_list = []
    for i in json_data:
        try:
            single_startup = {"num": i, "amount": json_data[i]['amount'], "round": json_data[i]['round'], 
                                "industries": json_data[i]['industries'], "page_count": json_data_2[i]['page_count'],
                                "fonts": json_data_2[i]['fonts'], "colors": json_data_2[i]['colors'], "text": json_data_2[i]['text']}
            master_list.append(single_startup)
        except:
            print("invalid")
            pass
    return master_list


def write_results(filename, dataset):
    f = open(filename, "w+")
    json.dump(dataset, f, indent=2)
    f.close()
    print("Exported to JSON.")
    