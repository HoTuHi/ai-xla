import cv2,time
import  numpy
import glob
# -----------------------------------------------------
# ---------            read IMG          --------------
# -----------------------------------------------------
path = "texture.png"
img = cv2.imread(path)
scale = 0.5
img = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))
# -----------------------------------------------------
# --------- test                         --------------
# -----------------------------------------------------


# -----------------------------------------------------
# --------- test                         --------------
# -----------------------------------------------------
def sobelCongactotal(img):
    ddepth = cv2.CV_16S
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    offsetX = cv2.Sobel(imgGray, ddepth, 1, 0, ksize=1, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    offsetY = cv2.Sobel(imgGray, ddepth, 0, 1, ksize=1, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

    resX = cv2.convertScaleAbs(offsetX)
    resY = cv2.convertScaleAbs(offsetY)

    res = cv2.addWeighted(resX,0.5, resY, 0.5, 0)
    return res

def saveVideo():
    autoBeatyImg(img)
    img_array = []
    for filename in glob.glob('tov/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def autoBeatyImg(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(imgHSV)
    for i in range (1,200,2):
        h[h>0] = i
        s[s<20] = 200
        res = cv2.merge((h,s,v))
        res =cv2.cvtColor(res,cv2.COLOR_HSV2RGB)
        cv2.imwrite("tov/res"+str(i)+".jpg",res)

def openVideo():
    cap = cv2.VideoCapture('project.avi')

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video  file")

    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break
cv2.imshow("src", img)
res = sobelCongactotal(img)
cv2.imshow("res", res)
openVideo()
cv2.waitKey(0)
cv2.destroyAllWindows()
