from cv2 import cv2 as cv 

#reading image 
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow(" bgr image",img)

#converting bgr to gray 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray image",gray)

#converting bgr to hsv 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv image",hsv)
 
#converting bgr to lab
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab image",lab)

#converting hsv to bgr 
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsv --> bgr",hsv_bgr)

#converting lab to bgr 
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("lab-->bgr",lab_bgr)

#converting bgr to rgb
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb image",rgb)

cv.waitKey(0)