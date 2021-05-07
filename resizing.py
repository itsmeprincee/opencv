from cv2 import cv2 as cv
def rescaling(frame,scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def livevideo(width,height):
    live.set(3,width)
    live.set(4,height)
#image reading
img = cv.imread("vijay.jpg")
resize1 = rescaling(img,scale=0.1)
cv.imshow("image",resize1)
#video reading
vid = cv.VideoCapture("vijay.mp4")
while True:
    isTrue,frames=vid.read()
    resize = rescaling(frames,scale=0.25)
    cv.imshow("video",resize)
    if cv.waitKey(20) == ord("d"):
        break
vid.release()
#live video
live = cv.VideoCapture(0)
while True:
    isTrue,frame = live.read()
    livevideo(200,300)
    cv.imshow("live video",frame)
    if cv.waitKey(20) == ord("d"):
        break
live.release()
cv.destroyAllWindows()
