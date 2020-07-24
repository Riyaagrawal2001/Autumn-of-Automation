import cv2
import numpy as numpy

cap = cv2.VideoCapture('tennis_balls.mov')


while cap.isOpened():
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx)<=15:
            cv2.drawContours(frame, [approx],0,(0,0,255),5)

        cv2.imshow("feed",frame)

        if cv2.waitKey(40)==27:
    	    break

cap.release()
cv2.destroyAllWindows()
