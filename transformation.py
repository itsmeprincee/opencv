from cv2 import cv2 as cv 
import numpy as np 
#creating blank image 
blank = np.zeros((500,1000,3),dtype="uint8")
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("vijay",img)

#1.paint the images with certain color
blank[:] = 255,255,0
cv.imshow("blank",blank)

#translationg the image
def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimens = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimens)
translated = translate(img,200,-200)
cv.imshow("translated image",translated)

#rotation of the image 
def rotate(img,angle,rpoint = None):
    (height,width) = img.shape[:2]
    if rpoint is None:
        rpoint = (width//2,height//2)
    rotmat = cv.getRotationMatrix2D(rpoint,angle,1.0)
    dimesnions = (width,height)
    return cv.warpAffine(img,rotmat,dimesnions)
rotated = rotate(img,45)
cv.imshow("rotate image",rotated)

#flipping the image 
flip = cv.flip(img,-1)
cv.imshow("flipped",flip)
cv.waitKey()