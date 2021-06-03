import cv2
import numpy as np
from cv2 import *
import RemoveHV as rm
import pytesseract
from collections import  Counter
from dfRec import findRec
import os, random

from transform import transfromToSquare
def generate_text(img):
    pytesseract.pytesseract.tesseract_cmd = "D:\\SteamGame\\New folder\\tesseract.exe"
    gray = np.array(img)
    gray = 255 * (gray < 128).astype(np.uint8)  # To invert the text to white
    coords = cv2.findNonZero(gray)  # Find all non-zero points (text)
    x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    image = img[y - 15:y + h + 15, x - 15:x + w + 15]
    concateImg = np.concatenate((image, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)

    try :
        text = pytesseract.image_to_string(concateImg)
        if len(text)>3:
            arrr = []
            arrr[:0]=text
            ctn = Counter(arrr)
            for aa in ctn:
                # if int(aa)>=1 and int(aa)<=9:
                return int(aa)
        else :
            return  0
    except Exception as e:
        return 0
def toStr(img, x=100):

    result = img.copy()
    img = rm.renmove_lines(img, x)
    img = cv2.resize(img, (900, 900))
    # cut the image to sigle number
    cell = [np.hsplit(row, 9) for row in np.vsplit(img, 9)]
    arr = []
    for i in cell:
    # print(len(i))
        x = []
        for j in i :
            x.append(int(generate_text(j)))
        arr.append(x)
    return arr

def img2str(path):
    if path == '':
        return
    else :
        path = random.choice(os.listdir("./data/p/")) # change dir name to whatever
        path = "./data/p/"+path
        # img = cv2.imread(path, 0)
        img1 = cv2.imread(path)
        ress= findRec(img1) #return npfloat32
        ress = cv2.cvtColor(ress,cv2.COLOR_BGR2GRAY)
        return toStr(ress)

if __name__ == '__main__':
    path = 'Untitled-1.png'
    # print(img2str(path))
    img = cv2.imread(path, 0)
    img1 = cv2.imread(path)
    try:
        ress= findRec(img1) #return npfloat32
        # print(aaaa)
        # ress = transfromToSquare(img1,aaaa)
        cv2.imshow("res",ress)
        ress = cv2.cvtColor(ress,cv2.COLOR_BGR2GRAY)
        toStr(ress)
        cv2.waitKey(0)
    except Exception as e:
        print("khum dc")