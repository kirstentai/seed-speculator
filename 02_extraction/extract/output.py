""" Write dictionary to json"""
import os
import json

def write_results(filename, dictionary):
    f = open(filename, "w")
    json.dump(dictionary, f)
    f.close()
    print("Dictionary successfully converted to JSON.")