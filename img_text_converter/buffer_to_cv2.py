import numpy as np
import cv2

def buffer_image_to_cv2_image(bfrimg): # bfrimg -> Buffer Image
    bfrimg = bfrimg.read() # read entire file into byte array
    np_array = np.frombuffer(bfrimg, dtype=np.uint8)
    cv2_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return cv2_img
