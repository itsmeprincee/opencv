from cv2 import cv2 as cv 
#reading images 
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("images",img)

#average 
avg = cv.blur(img,(3,3))
cv.imshow("average blur",avg)

#gaussian blur 
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("gauss",gauss)

#median blur 
median = cv.medianBlur(img,3)
cv.imshow("median",median)

#bilateral filter
bilateral = cv.bilateralFilter(img,35,35,25)
cv.imshow("bilateral",bilateral)
cv.waitKey(0)