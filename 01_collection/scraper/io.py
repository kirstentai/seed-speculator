""" Write dictionary to json"""
import os
import json


def write_results(filename, dictionary):
    f = open(filename, "w+")
    json.dump(dictionary, f, indent=2)
    # for d in list:
    # json.dumps(list)
    
    f.close()
    print("List successfully converted to JSON.")