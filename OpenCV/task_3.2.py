import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret,frame = cap.read()
	grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	grayframeInv = 255-grayframe

	grayframeInv1 = cv2.GaussianBlur(grayframeInv,(21,21),0)
	output = cv2.divide(grayframe,255-grayframeInv1,scale=256.0)
	cv2.imshow('video',output)

	if cv2.waitKey(1)&0xff==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()