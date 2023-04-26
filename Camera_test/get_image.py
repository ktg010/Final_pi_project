import cv2
import numpy as np
from PIL import *
import time

#take the picture
class Image:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.result, self.image = self.cap.read()

    def Display(self):
        if self.result:
            #show the image
            cv2.imshow("Yuh", self.image)

            #save the image
            cv2.imwrite(r"C:\Users\hambu\OneDrive\Desktop\Final_pi_project\Camera_test\Yuh.png", self.image)
            #raise Exception("Image could not be saved!")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

#get image dimensions
E = Image()
E.Display()

h, w, _ = E.image.shape
print('width: ', w)
print('height:', h)
print(E.result)



