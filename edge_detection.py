from cv2 import cv2 as cv 
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("images",img)


#gray image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#laplacian method 
lap = cv.Laplacian(gray,cv.CV_64F)
cv.imshow("laplacian edge ",lap)

#sobel method 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
#cv.imshow("sobel x",sobelx)
#cv.imshow("sobel y ",sobely)
sobel_combined = cv.bitwise_or(sobelx,sobely)
cv.imshow("sobel combined",sobel_combined)

#canny method 
canny = cv.Canny(gray,150,255)
cv.imshow("canny method",canny)
cv.waitKey(0)