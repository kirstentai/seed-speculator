""" This file extracts pdf details."""
import os.path
import fitz
import pdfplumber
import io
from PIL import Image

import cv2
import numpy as np
from skimage import io as skio
import matplotlib.pyplot as plt

def main():
    file_no = 5288
    start_number = 5288
    end_number = 5288 #5941 last
    while start_number <= file_no <= end_number: 

        try:
            file_path = get_filepath(file_no)
            print("Startup no.: ", file_no)
        except Exception:
            pass

        doc = fitz.Document(file_path)

        page_count = count_pages(doc)
        

        # for each page, extract text, download image, save image file names to list
        images_masterlist = []
        text_masterlist = []
        font_masterlist = []
        for current_page in range(page_count):
            page = extract_text_page(file_path, current_page)
            print(f"Page {current_page + 1}/{page_count}: {page}")
            text_masterlist.append(str(page))

            list_of_images = extract_download_image(file_no, doc, current_page)
            images_masterlist = images_masterlist + list_of_images

            if page is not None:
                page_font = extract_font(doc, current_page)
                font_masterlist.append(page_font)
        # print(f"image files: {images_masterlist}")
        
        colors_masterlist = []
        for img in images_masterlist:
            try:
                main_color = extract_image_color(img)
                colors_masterlist.append(list(main_color))

            except:
                print("Unable to get color.")
                pass
        
        print(f"====== Summary: {file_no} ======")
        print(f"Page count: {page_count}") if page_count else print("No PDF.")
        print(f"font master: {font_masterlist}")
        
        colors_dict = {str(rgb_color):colors_masterlist.count(rgb_color) for rgb_color in colors_masterlist}
        print(f"color schemes: {colors_dict}")
        print(f"text master: {text_masterlist}")
        file_no += 1


def get_filepath(file_number):
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    parent_directory_2 = os.path.split(parent_directory)[0]

    filename = str(file_number) + '.pdf'
    filepath = os.path.join(parent_directory_2, '01_collection', filename)

    if os.path.exists(filepath): 
        return filepath
    else:
        return None


def count_pages(document):
    count = document.page_count
    return count


def extract_text_page(filepath, page_number):
    with pdfplumber.open(filepath) as pdf:
        page = pdf.pages[page_number]
        return page.extract_text()


def extract_download_image(startup_number, document, page_number):
    # get page itself
    page = document[page_number]
    image_list = page.get_images()

    # print number of images found in current page
    if image_list:
        print(f"[+] Found {len(image_list)} images in page {page_number+1}.")
    else:
        print(f"[!] No image found.")
    
    image_download_list = []
    for image_index, img in enumerate(page.get_images(), start=1):

        xref = img[0]
        base_image = document.extract_image(xref)
        image_bytes = base_image["image"]

        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        image_filename = f"{startup_number}_img{page_number+1}.{image_index}.{image_ext}"

        #save image to local
        image.save(open(image_filename, "wb"))
        #append file names of downloaded images to list
        image_download_list.append(image_filename)
    
    return image_download_list


def extract_font(document, page_number):
    font_list = document.get_page_fonts(page_number)
    # print(f"fonts: {font_list}")
    return font_list


def extract_image_color(filename):
    img = skio.imread(filename)[:, :, :-1]
    # print(f"img: {img}")

    # calculate the mean of each chromatic channel 
    average = img.mean(axis=0).mean(axis=0)

    # apply k-means clustering to create a palette
    pixels = np.float32(img.reshape(-1, 3))
    n_colors = 3
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    dominant = palette[np.argmax(counts)]
    # print(f"dominant color: {dominant}")
    return dominant

main()
