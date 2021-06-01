import cv2
import  pytesseract
import numpy as np

def generate_text(img):
    image = np.array(img)
    # gray = 255 * (gray < 128).astype(np.uint8)  # To invert the text to white
    # coords = cv2.findNonZero(gray)  # Find all non-zero points (text)
    # x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    # image = img[y - 15:y + h + 15, x - 15:x + w + 15]
    concateImg = np.concatenate((image, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    return pytesseract.image_to_string(concateImg)

pytesseract.pytesseract.tesseract_cmd ="D:\\SteamGame\\New folder\\tesseract.exe"
img = cv2.imread('Untitled-1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(generate_text(img))

def generate_text(img):
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
    return pytesseract.image_to_string(concateImg)

cv2.imshow("res",img)
cv2.waitKey(0)