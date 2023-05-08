import cv2
import numpy as np
from PIL import *
import time

#take the picture
class Image:
    def __init__(self):
        self.cap = cv2.VideoCapture(-1)
        self.result, self.image = self.cap.read()

    def Display(self):
        if self.result:
            #save the image
            cv2.imwrite(r"/home/pi/Desktop/Glass_Final_Project/glass_refactored/glassy/Yuh.png", self.image)
            

