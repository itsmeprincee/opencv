from cv2 import cv2 as cv 
import numpy as np 
#creating blank image 
blank = np.zeros([400,400,3],dtype="uint8")
cv.imshow("blank images",blank)
#rectangle box 
rect = cv.rectangle(blank.copy(),(30,30),(370,370),(255),-1)
#cv.imshow("rectangle",rect)
circle = cv.circle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2),200,(255,255,255),-1)
#cv.imshow("circle",circle)

#bitwise and operation 
bit_and = cv.bitwise_and(rect,circle)
cv.imshow("bit_and",bit_and)

#bitwise or operation 
bit_or = cv.bitwise_or(rect,circle)
cv.imshow("bit_or",bit_or)

#bitwise xor operation 
bit_xor = cv.bitwise_xor(rect,circle)
cv.imshow("bit_xor",bit_xor)

#bitwise not operation 
bit_not = cv.bitwise_not(rect)
cv.imshow("bit_not",bit_not)
cv.waitKey(0)