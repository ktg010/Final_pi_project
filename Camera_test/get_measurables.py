#from get_image import *
import cv2
from math import *

#iterable to count how many points have been measured
n = 0
#create a point where the user clicked
def click(event, x, y, flags, params):
    global n
    #check for left mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        if n == 0:
            n += 1
            print(f'({x},{y})')
            global x1
            x1 = x
            global y1
            y1 = y

            # put coordinates as text on the image
            cv2.putText(image, f'({x},{y})',(x,y),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # draw point on the image
            cv2.circle(image, (x,y), 3, (0,255,255), -1)

        elif n == 1:
            n += 1
            print(f'({x},{y})')
            global x2
            x2 = x
            global y2
            y2 = y

            # put coordinates as text on the image
            cv2.putText(image, f'({x},{y})',(x,y),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # draw point on the image
            cv2.circle(image, (x,y), 3, (0,255,255), -1)
            #print info about points
            print(f"Point 1: ({x1},{y1})\nPoint 2: ({x2},{y2})\nDistance between points: {distance(x1,y1,x2,y2,'A')}")
        else:
            pass

    if event == cv2.EVENT_RBUTTONDOWN:
        pass

#find distance between two points
def distance(x1,y1,x2,y2,block):
    pixel_distance = sqrt(abs((x2-x1))^2+abs((y2-y1))^2)
    if block == "A":
        realdist = 5
        realunit = "inches"
        actual_dist = "Placeholder"
    return (str(pixel_distance) + " " + realunit)






image = cv2.imread("Yuh.png")

# create window
cv2.namedWindow("Point coordinates")

# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback("Point coordinates", click)

#Display image
while True:
    cv2.imshow("Point coordinates", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# close the window
cv2.destroyAllWindows()
