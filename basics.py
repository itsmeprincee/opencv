from cv2 import cv2 as cv
img = cv.imread("car.jpg")
#resize 
img = cv.resize(img,(1000,600),interpolation= cv.INTER_AREA)
cv.imshow("image",img)
#converting normal image to gray scale image
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",grey)
#blur images
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("blur image",blur)
# the edges using canny
edges = cv.Canny(blur,125,255)
cv.imshow("edges",edges)
#dilated the images 
dilated = cv.dilate(edges,(1,1),iterations=1)
cv.imshow("dilated",dilated)
#erdode the image
eroded = cv.erode(dilated,(1,1),iterations=1)
cv.imshow("eroded",eroded)
#cropped the image
cv.imshow("cropped",eroded[100:200,300:400])
cv.waitKey()
