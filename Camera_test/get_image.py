import cv2
import numpy as np
from PIL import *
import time

cap = cv2.VideoCapture(0)
result, image = cap.read()

if result:
    cv2.imshow("Yuh", image)

    cv2.imwrite("Camera_test/Yuh.png", image)

    cv2.waitKey(0)
    cv2.destroyWindow("Yuh")

h, w, _ = image.shape
print('width: ', w)
print('height:', h)




