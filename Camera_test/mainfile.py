from get_measurables import *
from get_image import *

E = Image()
E.Display()

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
