""" Sentiment analysis on pdf text"""
import json



def main():
    # read in json files
    file_name = 'output_final.json'
    f = open(file_name)
    data = json.load(f)

    # extracting text per startup, list of strings
    for startup in data['startup_info']:
        if startup['num'] == '5286':
            print(startup['text']) # list type


main()  