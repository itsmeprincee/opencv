from cv2 import cv2 as cv 
import numpy as np 
#reading image 
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("image",img)
#blank image 
blank = np.zeros((500,1000,3),dtype="uint8")
cv.imshow("blank",blank)
#spliting into parts 
b,g,r = cv.split(img)
#displaying different splitted images 
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)

#merging these images 
merged = cv.merge([b,g,r])
cv.imshow("merged image",merged)

##print(b.shape,g.shape,r.shape)
cv.waitKey(0)