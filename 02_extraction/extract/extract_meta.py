""" This file extracts pdf details."""
import os.path
import fitz
import pdfplumber


def main():
    
    file_no = 5285
    while file_no >= 5285 and file_no <= 5287: #5941 last
        file_path = get_filepath(file_no)
        doc = fitz.Document(file_path)
        
        print("Startup no.: ", file_no)

        page_count = count_pages(doc)
        print(f"page count: {page_count}") # starts pg 0 to page_count - 1

        for n in range(page_count):
            current_page = extract_text_page(file_path, n)
            print(f"Page {n}/{page_count}: {current_page}")

        file_no += 1


def get_filepath(file_number):
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    parent_directory_2 = os.path.split(parent_directory)[0]

    FILE = str(file_number) + '.pdf'
    filepath = os.path.join(parent_directory_2, '01_collection', FILE)

    return filepath


def count_pages(document):
    count = document.page_count
    return count


def extract_text_page(filepath, page_num):
    with pdfplumber.open(filepath) as pdf:
        page = pdf.pages[page_num]
        return page.extract_text()    

main()