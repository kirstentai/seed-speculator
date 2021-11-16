import fitz
import os.path

current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
parent_directory_2 = os.path.split(parent_directory)[0]
filename = '5286.pdf'
file_path = os.path.join(parent_directory_2, '01_collection', filename)

print(file_path)

doc = fitz.Document(file_path)


pdf_metadata = doc.metadata
print(pdf_metadata)


page_count = doc.page_count
print("page count: {}".format(page_count))


read_page = doc.load_page(1)
print("read page: {}".format(read_page))


# #extract table of content
pdf_toc = doc.get_toc()
print("toc: {}".format(pdf_toc))


# # extract links from a page
for page in doc:
    plink = page.get_links()
    print("{} | links: {}".format(page, plink))
