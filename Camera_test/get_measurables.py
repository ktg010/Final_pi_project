from get_image import *
import cv2
from math import *

#class for collecting measurement data about block
class Measurables:
    def __init__(self, image):
        self.image = cv2.imread(image)
        self.n = 0

    #str method
    def __str__(self):
        print(f"Point 1: ({self.x1},{self.y1})\nPoint 2: ({self.x2},{self.y2})\nDistance between points: {self.distance(self.x1,self.y1,self.x2,self.y2,'A')}")



    #create a point where the user clicked
    def click(self, event, x, y, flags, params):
        #check for left mouse click
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.n == 0:
                self.n += 1
                print(f'({x},{y})')
                self.x1 = x
                self.y1 = y

                # put coordinates as text on the image
                cv2.putText(self.image, f'({x},{y})',(x,y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # draw point on the image
                cv2.circle(self.image, (x,y), 3, (0,255,255), -1)

            elif self.n == 1:
                self.n += 1
                print(f'({x},{y})')
                self.x2 = x
                self.y2 = y
                self.__str__()
                # put coordinates as text on the image
                cv2.putText(self.image, f'({x},{y})',(x,y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                # draw point on the image
                cv2.circle(self.image, (x,y), 3, (0,255,255), -1)
                #print info about points
            else:
                pass


#find distance between two points
    def distance(self,x1,y1,x2,y2,block):
        x_diff = x2-x1
        y_diff = y2-y1
        print(x_diff)
        pixel_distance = sqrt(x_diff**2+y_diff**2)
        if block == "A":
            conversion_rate = (35.62)
            real_distance = (pixel_distance/conversion_rate)
            realunit = "inches"
            print(pixel_distance)
        return (str(real_distance) + " " + realunit)


#instantiate image for measurables
M = Measurables("Yuh.png")


# create window
cv2.namedWindow("Point coordinates")

# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback("Point coordinates", M.click)

#Display image
while True:
    cv2.imshow("Point coordinates", M.image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
print(M.distance(1,0,5,0,'A'))
# close the window
cv2.destroyAllWindows()
