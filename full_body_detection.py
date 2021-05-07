from cv2 import cv2 as cv 
img = cv.imread("images/group.jpg")
img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#img = cv.resize(img,(1200,500),interpolation=cv.INTER_AREA)
#cv.imshow("vijay photo",img)


#converting gray image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray image",gray)

#face cascade classifer 
face_cascaded = cv.CascadeClassifier("haar_frontal_face.xml")
face_rect = face_cascaded.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
print(f"no of faces found {len(face_rect)}")

# lower body cascade classifier 
har_cascade = cv.CascadeClassifier("haarcascade_fullbody.xml")
lower_rect = har_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f"no of lower body found {len(lower_rect)}")

#displaying image with face detection 
for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
for(x,y,w,h) in lower_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("face_detected photo",img)
cv.waitKey(0)