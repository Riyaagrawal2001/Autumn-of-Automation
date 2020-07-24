import cv2
import numpy as np 

image = cv2.imread('plant.jpg',0)
cv2.imshow('original',image)

laplacian = cv2.Laplacian(image,cv2.CV_32F)
cv2.imshow('laplacian',laplacian)

edges1 = cv2.Canny(image,100,200)
cv2.imshow('edges1',edges1)

laplacian1 = cv2.Laplacian(edges1,cv2.CV_32F)
cv2.imshow('laplacian1',laplacian1)

image1 = 255-edges1
cv2.imshow('sketch',image1)

cv2.waitKey(0)
cv2.destroyAllWindows()