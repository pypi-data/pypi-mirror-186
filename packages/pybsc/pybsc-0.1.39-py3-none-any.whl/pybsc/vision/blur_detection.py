import cv2
import numpy as np


def estimate_blur(img):
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur_map = cv2.Laplacian(img, cv2.CV_64F)
    score = np.var(blur_map)
    return blur_map, score


def calculate_blur_map(blur_map, blur_sigma=5,
                       median_blur_sigma=5, min_abs=0.5):
    abs_image = np.abs(blur_map).astype(np.float32)
    abs_image[abs_image < min_abs] = min_abs
    abs_image = np.log(abs_image)
    abs_image = cv2.blur(abs_image, (blur_sigma, blur_sigma))
    abs_image = np.array(abs_image, dtype=np.uint8)
    return cv2.medianBlur(abs_image, median_blur_sigma)
