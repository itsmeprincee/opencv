from cv2 import cv2 as cv 
import numpy as np 
img = cv.imread("vijay.jpg")
img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("vijay",img)
#creating blank image 
blank = np.zeros(img.shape[:2],dtype="uint8")
#creating circle 
circle = cv.circle(blank.copy(),(img.shape[1]//2-30,img.shape[0]//2-50),100,100,-1)
cv.imshow("circle",circle)
#creating mask 
masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow("masked",masked)
cv.waitKey(0)