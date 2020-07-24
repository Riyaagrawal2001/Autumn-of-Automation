import cv2
import numpy as np 

MIN_MATCH_COUNT = 10
sift = cv2.xfeatures2d.SIFT_create()

img = cv2.imread('ball.png',0)
kp1, des1 = sift.detectAndCompute(img,None)

cap = cv2.VideoCapture('tennis_balls.mov')

while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	kp2, des2 = sift.detectAndCompute(gray, None)

	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
	search_params = dict(checks=50)

	flann = cv2.FlannBasedMatcher(index_params, search_params)
	matches = flann.knnMatch(des1, des2, k=2)

	good = []
	for m,n in matches:
		if m.distance<0.7*n.distance:
			good.append(m)

	if len(good)>MIN_MATCH_COUNT:
		src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
		dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
		matchesMask = mask.ravel().tolist()

		h, w = img.shape[:2]
		pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
		dst = cv2.perspectiveTransform(pts, M)

		frame = cv2.polylines(frame,[np.int32(dst)],True, 255,3,cv2.LINE_AA)

	else:
		print ("Not enough matches are found - %d/%d"%(len(good, MIN_MATCH_COUNT)))
		matchesMask = None

	draw_params = dict(matchColor=(0,255,0),singlePointColor=None,matchesMask=matchesMask,flags=2)
	image = cv2.drawMatches(img,kp1,frame,kp2,good,None,**draw_params)
	cv2.imshow('plot', image)

	if cv2.waitKey(40)==27:
		break

cap.release()
cv2.destroyAllWindows()








