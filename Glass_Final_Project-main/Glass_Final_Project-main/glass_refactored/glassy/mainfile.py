from glassy.get_measurables import *
from glassy.get_image import *

def func():

    #Take/save image
    E = Image()
    E.Display()

    #access image to measure langth of hypotenuse
    M = Measurables("/home/pi/Desktop/Glass_Final_Project/glass_refactored/glassy/Yuh.png")


    # create window
    cv2.namedWindow("Point coordinates")


    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback("Point coordinates", M.click)

    print("Hello")
    #Display image
    while True:
        cv2.imshow("Point coordinates", M.image)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            INDEX = M.n
            for i in range(1,5):
                cv2.waitKey(0)
            break
    return M.__str__
