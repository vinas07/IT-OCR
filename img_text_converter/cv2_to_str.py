from .buffer_to_cv2 import buffer_image_to_cv2_image
import numpy as np
import cv2
import easyocr

def extract_text(bfrimg):
    cv2_img = buffer_image_to_cv2_image(bfrimg)
    reader = easyocr.Reader(['en'], gpu=False)
    text = reader.readtext(cv2_img)
    return text

