from cv2 import cv2 as cv
#reading images..
img = cv.imread("vijay.jpg")
resize = cv.resize(img,(200,300))
cv.imshow("image",resize)
#reading videos
capture = cv.VideoCapture("vijay.mp4")
while True:
    isTrue,frame = capture.read()
    cv.imshow("video",frame)
    if cv.waitKey(20) == ord("d"):
        break
capture.release()
cv.destroyAllWindows()
