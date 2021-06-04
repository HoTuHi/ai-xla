import cv2
import test
from  dfRec import  findRec



def findRec(image):
    cascade = cv2.CascadeClassifier('./data/classifier/cascade.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    samp = cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in samp:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Resize and convert to grayscale
        # img = cv2.cvtColor(resize(image), cv2.COLOR_BGR2GRAY)
    return test.haarCascade(image)
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
            break



path = "./data/demo.png"
img = cv2.imread(path)
cv2.imshow('raw',img)
cv2.imshow('res',findRec(img))
cv2.waitKey(0)
cv2.destroyAllWindows()