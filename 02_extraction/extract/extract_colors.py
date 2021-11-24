import cv2
import numpy as np
from skimage import io

# image_file = f"{str(startup_no)}_img
img = io.imread('5288_img1.1.png')[:, :, :-1]

# calculate the mean of each chromatic channel 
average = img.mean(axis=0).mean(axis=0)

# apply k-means clustering to create a palette
pixels = np.float32(img.reshape(-1, 3))
n_colors = 5
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
_, counts = np.unique(labels, return_counts=True)

dominant = palette[np.argmax(counts)]
print(f"dominant color: {dominant}")