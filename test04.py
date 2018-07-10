import cv2
import numpy as np

img = cv2.imread("test01.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,100,100])
upper_blue = np.array([130,255,255])

lower_green = np.array([60,100,100])
upper_green = np.array([70,255,255])

lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])

red_mask = cv2.inRange(hsv,lower_red,upper_red)
green_mask = cv2.inRange(hsv,lower_green,upper_green)
blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)

red = cv2.bitwise_and(img,img,mask=red_mask)
green = cv2.bitwise_and(img,img,mask=green_mask)
blue = cv2.bitwise_and(img,img,mask=blue_mask)

res = green + red + blue 

cv2.imshow('img',res)

cv2.waitKey(0)

cv2.destroyAllWindows()
