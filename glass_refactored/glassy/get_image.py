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
            #save the image
            cv2.imwrite(r"/home/pi/Desktop/Final_project/Final_pi_project/Camera_test/Yuh.png", self.image)
            
E = Image()
E.Display()



