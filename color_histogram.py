from cv2 import cv2 as cv 
import matplotlib 
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt 
import numpy as np 


#reading images 
img = cv.imread("car.jpg")
img = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("image",img)

#creating blank image 
blank = np.zeros(img.shape[:2],dtype="uint8")

#creating circle 
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),250,(255,255,255),-1)

#creating mask 
mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow("masked image",mask)

#calculating histograms 
plt.figure()
plt.title("color histograms")
plt.xlabel("bins")
plt.ylabel("no of pixels")
colors = ["b","g","r"]
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)