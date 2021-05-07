from cv2 import cv2 as cv 
img = cv.imread("images/car.jpg")
img = cv.resize(img,(1200,500),interpolation=cv.INTER_AREA)
#cv.imshow("vijay photo",img)


#converting gray image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray image",gray)

#cascade classifier 
har_cascade = cv.CascadeClassifier("haarcascade_license_plate.xml")
face_rect = har_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
print(f"no of faces found {len(face_rect)}")

#displaying image with face detection 
for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("face_detected photo",img)
cv.waitKey(0)