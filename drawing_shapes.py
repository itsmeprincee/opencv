from cv2 import cv2 as cv
import numpy as np
#image loading
img = cv.imread("vijay.jpg")
resize = cv.resize(img,(400,400))
resize[100:300,300:400] = 0,0,255
cv.imshow("vijay",resize)
#creating empyt image
nimg = np.zeros((500,500,3),"uint8")
#paint the image with a certain color
nimg[0:nimg.shape[1]//2,0:nimg.shape[0]//2] = 0,255,0
#creating a rectanle
#cv.rectangle(nimg,(0,0),(500,500),(255,255,255),thickness=-1)
cv.rectangle(nimg,(250,250),(500,500),(0,0,255),thickness =-1)
#Creating a circle
cv.circle(nimg,(250,250),50,(255,0,0),thickness=cv.FILLED)
#drawing a circle
cv.line(nimg,(0,0),(500,500),(255,0,255),thickness=3)
#writing text in images
cv.putText(nimg,"Vijay~King of Queens",(10,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow("empty image",nimg)
cv.waitKey(0)
