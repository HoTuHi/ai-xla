import cv2
import numpy as np
from transform import transfromToSquare


def resize(img, height=800):
    """ Resize image to given height """
    rat = height / img.shape[0]
    return cv2.resize(img, (int(800), height))

def findRec(image):
    # Resize and convert to grayscale
    img = cv2.cvtColor(resize(image), cv2.COLOR_BGR2GRAY)

    # Bilateral filter preserv edges
    img = cv2.bilateralFilter(img, 9, 75, 75)
    img = cv2.medianBlur(img, 11)
    edges = cv2.Canny(img, 200, 250)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    ress = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    # loop over our contours
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            aaa = np.float32([approx[0],approx[3],approx[1],approx[2]])
            ress = transfromToSquare(resize(image), aaa)
            cv2.imshow("sample",ress)
            return ress
            break
