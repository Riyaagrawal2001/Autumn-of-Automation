import cv2

image = cv2.imread('strawberries.jpg')
cv2.imshow('original',image)

img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('converted',img)

if cv2.waitKey(0)&0xff==27:
	cv2.destroyAllWindows()