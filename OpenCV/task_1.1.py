import cv2
import numpy as np 

image = cv2.imread('plant.jpg')
cv2.imshow('original',image)

img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',img)

thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)
cv2.imshow('adaptive_gaussian',thresh)

if cv2.waitKey(0)&0xff==27:
	cv2.destroyAllWindows()

