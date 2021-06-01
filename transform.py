import cv2
import numpy as np
def transfromToSquare(frame,pts1):
    h,w,_= frame.shape
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (w, h))
    return result