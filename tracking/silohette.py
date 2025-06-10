
import cv2

def hog():
    img = cv2.imread("./hepburn.png")

    # create HOG person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # detect people
    boxes, _ = hog.detectMultiScale(img,winStride=(8,8),padding=(8,8),scale=1.05)

    # draw rectangles
    for (x,y,w,h) in boxes:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)

    # show result
    cv2.imshow("Detected People", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

hog()

