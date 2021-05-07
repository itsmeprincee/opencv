from cv2 import cv2 as cv 

#reading images 
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("image",img)


#converting to gray scale image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple threshold 
threshold ,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simple threshold image",thresh)

#simple threshold inverse 
threshold ,thresh_inv = cv.threshold(gray,170,255,cv.THRESH_BINARY_INV)
cv.imshow("simple threshold inverse image",thresh_inv)


#adapative threshold 
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive threshold",adaptive_thresh)

#adaptive theshold inverse 
adaptive_thresh_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow("adaptive threshold inverse ",adaptive_thresh_inv)

#adaptive threshold gaussian 
adaptive_gaussian = cv.adaptiveThreshold(gray,256,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive gaussian ",adaptive_gaussian)
cv.waitKey(0)