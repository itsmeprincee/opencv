from cv2 import cv2 as cv 
import numpy as np 
blank = np.zeros((500,1000,3),dtype="uint8")
car = cv.imread("car.jpg")
car = cv.resize(car,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("car photo",car)

#gray scale image 
gray = cv.cvtColor(car,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image",gray)

#blur the gray image
blur = cv.GaussianBlur(gray,(1,1),cv.BORDER_DEFAULT)
cv.imshow("blur image",blur)

#finding edges 
canny = cv.Canny(blur,125,175)
cv.imshow("edging",canny)

#finding contours 
contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found")

#drawing into another image 
cv.drawContours(blank,contours,-1,(0,0,255),-1)
cv.imshow("blank image",blank)
cv.waitKey(0)