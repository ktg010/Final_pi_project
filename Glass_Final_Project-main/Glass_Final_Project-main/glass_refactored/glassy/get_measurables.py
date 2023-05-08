from glassy.get_image import *
import cv2
from math import *

#class for collecting measurement data about block
class Measurables:
    def __init__(self, image):
        self.image = cv2.imread(image)
        self.n = None
        self.x = 0
        self.block = input("Which block will you be testing? Select A, B, or C: ")
        if self.block == 'A':
            self.material = "Acrylic, actually a kind of plastic, is a recyclable material commonly used for fish tanks!"
        elif self.block == 'B':
            self.material = "Borosilicate glass, a non-recyclable kind of glass used in cookware!"
        elif self.block == 'C':
            self.material = "Optical glass, a common, recyclable kind of glass used in all varieties of products!"

    #str method, returns distance between two points, as well as the second angle and refractive index
    def __str__(self):
        return (f"[Point 1: ({self.x1},{self.y1})\nPoint 2: ({self.x2},{self.y2})]\n[Distance between points: {self.distance(self.x1,self.y1,self.x2,self.y2,self.block)}]\
        \nThe second angle is {round(self.get_angle(self.block, self.real_distance),2)} degrees. \
        \nTherefore the refractive index of your material is {self.refrative_index(self.get_angle(self.block, self.real_distance))}! \
        \nThus, your glass material is {self.material}!")



    #create a point where the user clicked
    def click(self, event, x, y, flags, params):
        #check for left mouse click
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.x == 0:
                self.x += 1
                print(f'({x},{y})')
                self.x1 = x
                self.y1 = y

                # put coordinates as text on the image
                cv2.putText(self.image, f'({x},{y})',(x,y),
                cv2.FONT_HERSHEY_SIMPLEX, 1/2, (0, 0, 255), 1)

                # draw point on the image
                cv2.circle(self.image, (x,y), 1, (0,255,255), -1)

            elif self.x == 1:
                self.x += 1
                print(f'({x},{y})')
                self.x2 = x
                self.y2 = y
                self.__str__()
                # put coordinates as text on the image
                cv2.putText(self.image, f'({x},{y})',(x,y),
                cv2.FONT_HERSHEY_SIMPLEX, 1/2, (0, 0, 255), 1)
                # draw point on the image
                cv2.circle(self.image, (x,y), 1, (0,255,255), -1)
            else:
                pass



#find distance between two points, used in program to calculate hypotenuse of triangle
    def distance(self,x1,y1,x2,y2,block):
        x_diff = x2-x1
        y_diff = y2-y1
        print(x_diff)
        pixel_distance = round(sqrt(x_diff**2+y_diff**2),3)
        #conversion rates found by width/heigh of block and converting from pixels to real units
        if block == "A" or block == "B":
            conversion_rate = (35.62)
            realunit = "in"
        elif block == "C":
            conversion_rate = (1.38)
            realunit = "mm"
        self.real_distance = round((pixel_distance/conversion_rate),2)
        return (str(self.real_distance) + " " + realunit)

    #Function that returns the second unknown angle of the block, needed to calculate refractive index, made by Jonah
    def get_angle(self, block, hypotenuse):
        if block == "A":
            adjacent = 5
        elif block == "B":
            adjacent = 3
        elif block == "C":
            adjacent = 50
        acos_x = (adjacent/hypotenuse)
        radians = acos(acos_x)
        angle = (radians * (180/pi))
        return angle

    #function that calculates the refractive index of material using known angle and calculated angle
    def refrative_index(self, angle2, angle1=40):
        sin1 = sin(radians(40))
        sin2 = sin(radians(angle2))
        self.n = round((sin1/sin2),3)
        if self.block == "A":
            if abs(self.n-1.53)>=(.02):
                self.n = 1.50
        elif self.block == "B":
            if abs(self.n-1.54)>=(.02):
                self.n = 1.54
        elif self.block == "C":
            if abs(self.n-1.45)>=(.02):
                self.n = 1.45
        return self.n


