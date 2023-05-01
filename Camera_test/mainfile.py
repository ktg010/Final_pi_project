from get_measurables import *
from get_image import *

#Take/save image
E = Image()
E.Display()

#access image to measure langth of hypotenuse
M = Measurables("Camera_test/Yuh.png")


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
        cv2.destroyAllWindows()
        INDEX = M.n
        print(INDEX)
        for i in range(1,5):
            cv2.waitKey(0)
        break

