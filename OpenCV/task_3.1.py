import cv2

image = cv2.imread('plant.jpg')

grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
grayImageInv = 255-grayImage

grayImageInv2 = cv2.GaussianBlur(grayImageInv,(21,21),0)

output = cv2.divide(grayImage, 255-grayImageInv2, scale=256.0)

cv2.imshow('original',image)
cv2.imshow('sketch',output)

if cv2.waitKey(0)&0xff==27:
	cv2.destroyAllWindows()