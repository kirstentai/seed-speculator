""" This file extracts pdf details."""
import os.path
import fitz
import pdfplumber
from PIL import Image


def main():
    file_no = 5285
    while 5285 <= file_no <= 5287: #5941 last
        file_path = get_filepath(file_no)
        doc = fitz.Document(file_path)

        print("Startup no.: ", file_no)

        page_count = count_pages(doc)
        print(f"page count: {page_count}") # starts pg 0 to page_count - 1

        for current_page in range(page_count):
            page = extract_text_page(file_path, current_page)
            print(f"Page {current_page}/{page_count}: {page}")

            extract_image(doc, current_page)

        file_no += 1


def get_filepath(file_number):
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    parent_directory_2 = os.path.split(parent_directory)[0]

    filename = str(file_number) + '.pdf'
    filepath = os.path.join(parent_directory_2, '01_collection', filename)

    return filepath


def count_pages(document):
    count = document.page_count
    return count


def extract_text_page(filepath, page_number):
    with pdfplumber.open(filepath) as pdf:
        page = pdf.pages[page_number]
        return page.extract_text()


def extract_image(document, page_number):

    # get page itself
    page = document[page_number]
    image_list = page.getImageList()

    # print number of images found in current page
    if image_list:
        print(f"[+] Found {len(image_list)} images in page {page_number}.")
    else:
        print(f"[!] No image found.")
    
    for image_index, img in enumerate(page.getImageList(), start=1):

        xref = img[0]
        base_image = document.extractImage(xref)
        image_bytes = base_image["image"]



main()
