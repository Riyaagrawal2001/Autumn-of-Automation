import cv2
import numpy as np 

image = cv2.imread('T.jpg')
cv2.imshow('original',image)
rows,cols = image.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
img1 = cv2.warpAffine(image,M,(cols,rows))
cv2.imshow('first',img1)

O = np.float32([[1,0,0],[0,1,-50]])
img2 = cv2.warpAffine(img1,O,(cols,rows))
cv2.imshow('second',img2)

N = np.float32([[1,0,0],[0,1,100]])
img3 = cv2.warpAffine(image,N,(cols,rows))
cv2.imshow('third',img3)

P = np.float32([[1,0,-100],[0,1,-50]])
img4 = cv2.warpAffine(img2,P,(cols,rows))
cv2.imshow('fourth',img4)

m = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
img5 = cv2.warpAffine(image,m,(cols,rows))
cv2.imshow('fifth',img5)

img6 = cv2.warpAffine(img1,m,(cols,rows))
cv2.imshow('sixth',img6)

img7 = cv2.warpAffine(img6,m,(cols,rows))
cv2.imshow('seventh',img7)

img8 = cv2.warpAffine(img4,m,(cols,rows))
cv2.imshow('eighth',img8)

average = cv2.blur(image,(5,5))
cv2.imshow('ninth',average)

gaussian = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('tenth',gaussian)

median = cv2.medianBlur(image,5)
cv2.imshow('eleventh',median)

bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('twelth',bilateral)

if cv2.waitKey(0)&0xff==27:
	cv2.destroyAllWindows()