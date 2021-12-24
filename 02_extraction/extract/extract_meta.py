""" This file extracts pdf details."""
import enum
import os.path
import fitz
import pdfplumber
import io
from PIL import Image

import cv2
import numpy as np
from skimage import io as skio
import matplotlib.pyplot as plt
from extract.output import write_results

def main():
    file_no = 5285
    end_number = 5942 #5942 last
    master_dict = {}
    while file_no <= end_number: 

        try:
            file_path = get_filepath(file_no)
            print(f"====== Extracting startup no.: {file_no} ======")
        except Exception:
            pass

        doc = fitz.Document(file_path)

        page_count = count_pages(doc)
        
        # for each page, extract text, download image, save image file names to list
        images_masterlist = []
        text_masterlist = []
        font_masterlist = []
        for current_page in range(page_count):
<<<<<<< HEAD
<<<<<<< HEAD
            page = extract_text_page(file_path, current_page)
            text_masterlist.append(str(page))
=======
=======
>>>>>>> 8552e2a (01, 02 sections minor modifications)
            if extract_text_page(file_path, current_page):
                page = extract_text_page(file_path, current_page)
                # print(f"Page {current_page + 1}/{page_count}: Text detected")
                text_masterlist.append(str(page))

                if page != 'None':
                    page_font = extract_font(doc, current_page)
                    font_masterlist = font_masterlist + page_font
                
<<<<<<< HEAD
>>>>>>> 8552e2a (01, 02 sections minor modifications)
=======
>>>>>>> 8552e2a (01, 02 sections minor modifications)

            list_of_images = extract_download_image(file_no, doc, current_page)
            images_masterlist = images_masterlist + list_of_images
                
        # consolidates all dominant colors detected in images, contains repeated inputs
        colors_masterlist, no_colors = consolidate_colors(images_masterlist)
        colors_dict = tally_list(colors_masterlist)

        fonts_dict = tally_list(font_masterlist)
        fonts_list = dict_to_list(fonts_dict)
        print(f"fonts: {fonts_list}")

        # print_results(file_no, page_count, images_masterlist, colors_masterlist, no_colors, fonts_list, colors_dict, text_masterlist)
        output_results(master_dict, file_no, page_count, fonts_list, colors_dict, text_masterlist)
        write_results("02_output.json", master_dict)
        file_no += 1
    
    
    # print(f"master: {master_dict}")

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
        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.split(current_directory)[0]
        image_path = parent_directory + '/images/' + image_filename
        # print(image_path)

        #save image to local
        image.save(open(image_path, "wb"))
        #append file names of downloaded images to list
        image_download_list.append(image_path)
    
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
    return dominant


def get_dominant_color(pil_img, palette_size=16):
    # Resize image to speed up processing
    img = pil_img.copy()
    img.thumbnail((100, 100))

    # Reduce colors (uses k-means internally)
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

    # Find the color that occurs most often
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]
    dominant_color = palette[palette_index*3:palette_index*3+3]

    return dominant_color


def consolidate_colors(image_list):
    colors_masterlist = []
    no_color = 0
    for image in image_list:
        try:
            main_color = extract_image_color(image)
            # print(f"[+] Color detected: {main_color}")
            colors_masterlist.append(list(main_color))
        except:
            # print("[!] Unable to get color.")
            no_color += 1
            pass

    return colors_masterlist, no_color


def tally_list(list):
    tally_dict = {str(unique_item):list.count(unique_item) for unique_item in list}
    return tally_dict


def dict_to_list(fonts_dict):
    keys_list = []
    for keys, values in fonts_dict.items():
        if values > 1:
            keys_list.append(keys)
            # print(f"values: {values}")
    
    return keys_list
    

def output_results(master_dict, startup_no, count, fonts, colors, text):

    # startup_dict = {'startup_number': startup_no, 'page_count': count, 'fonts': fonts, 'colors': colors, 'text': text}
    master_dict[startup_no] = {}
    master_dict[startup_no]['page_count'] = count
    master_dict[startup_no]['fonts'] = fonts
    master_dict[startup_no]['colors'] = colors
    master_dict[startup_no]['text'] = text
    # print("Master_dict updated.")
    # return master_dict


def print_results(file_no, page_count, images_masterlist, colors_masterlist, no_colors, fonts_list, colors_dict, text_masterlist):
    print(f"====== Summary: {file_no} ======")
    print(f"Page count: {page_count}") if page_count else print("No PDF detected.")

    if len(images_masterlist) != 0:
        print(f"Total images found: {len(images_masterlist)}") 
    
    if len(colors_masterlist) != 0 and no_colors != 0:
        print(f"{len(colors_masterlist)} colors detected, {no_colors} not.\n")

<<<<<<< HEAD
<<<<<<< HEAD
    if len(fonts_dict) != 0:
        print(f"Fonts tally: {fonts_dict}\n")
=======
    if len(fonts_list) != 0:
        print(f"Fonts: {fonts_list}\n")
>>>>>>> 8552e2a (01, 02 sections minor modifications)
=======
    if len(fonts_list) != 0:
        print(f"Fonts: {fonts_list}\n")
>>>>>>> 8552e2a (01, 02 sections minor modifications)

    if len(colors_dict) != 0:
        print(f"Colors: {colors_dict}\n")
    
    if len(text_masterlist) != 0:
        print(f"Consolidated text.")


# main()

