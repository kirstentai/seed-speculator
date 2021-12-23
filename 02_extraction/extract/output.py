""" Write dictionary to json"""
import os
import json

def write_results(filename, dictionary):
    f = open(filename, "w+")
    json.dump(dictionary, f, indent=2)
    f.close()
    print("Dictionary successfully converted to JSON.")