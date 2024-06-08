import cv2
import numpy as np 

img=cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)
_, threshold =cv2.threshold(img,245,255,cv2.THRESH_BINARY)

contours, _=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
	cv2.drawContours(img,[cnt],0,(0),5)
	
cv2.imshow("shapes",img)
cv2.imshow("threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()