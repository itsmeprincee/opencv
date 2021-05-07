from cv2 import cv2 as cv 
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt 
import numpy as np 

img = cv.imread("vijay.jpg")
img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#cv.imshow("image",img)
blank = np.zeros(img.shape[:2],dtype="uint8")


#gray scale image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)


#circle 
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,(255,255,255),-1)
masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow("masked",masked)
gray_hist = cv.calcHist([gray],[0],masked,[256],[0,256])


#displaying gray_hist 
plt.figure()
plt.title("gray scale histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels ")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)