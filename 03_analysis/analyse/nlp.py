""" Sentiment analysis on pdf text"""
import json
import os.path


def main():
    # read in json files
    file_name = 'output_final.json'
    file_path = get_filepath(file_name)
    f = open(file_path)
    data = json.load(f)

    # extracting text per startup, list of strings
    for startup in data['startup_info']:
        if startup['num'] == '5286':
            print(startup['text']) # list type


def get_filepath(filename):
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    filepath = os.path.join(parent_directory, filename)

    if os.path.exists(filepath): 
        return filepath
    else:
        return None

main()  