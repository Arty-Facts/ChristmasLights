import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
from scipy.ndimage.filters import gaussian_filter
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def get_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        return None
    cam.release()
    return frame 

def find_light(img_gray):
    img=gaussian_filter(img_gray, sigma=5)
    result = np.where(img == np.amax(img))    
    for x, y in zip(*result):
        return x, y

def show_region(img, x, y, d=50):
    plt.imshow(img[x-d:x+d, y-d:y+d]) 

def show(img):
    plt.imshow(img)


