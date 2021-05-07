#importing libaraires 
from cv2 import cv2 as cv 
#resizing method 
def resizedMethod(frame,scale=1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0])
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#method for face detection 
def face_detection(resized_frame):
    #converting into gray scale image 
    gray = cv.cvtColor(resized_frame,cv.COLOR_BGR2GRAY)
    har_cascade = cv.CascadeClassifier("haar_frontal_face.xml")
    face_rect = har_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        cv.rectangle(resized_frame,(x,y),(x+w,y+h),(0,255,0),5)

#reading live video 
capture_video = cv.VideoCapture(0)

#displaying every frame in video 
while True:
    isTrue , frame = capture_video.read()
    resized_frame = resizedMethod(frame,scale=1)
    face_detection(resized_frame)
    cv.imshow("live video",resized_frame)
    if cv.waitKey(20) == ord("d"):
        break 


#releasing the camera 
capture_video.release()
cv.destroyAllWindows()