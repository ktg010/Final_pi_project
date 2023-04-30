from get_measurables import *
from get_image import *

#Take/save image
E = Image()
E.Display()

#access image to measure langth of parabola
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
