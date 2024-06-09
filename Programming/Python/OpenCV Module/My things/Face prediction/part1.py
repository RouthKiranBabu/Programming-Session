import cv2
import numpy as np 

face_xml_file='C:/Users/user/Desktop/Minor Project/My things/xml file/haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(face_xml_file)
eye_xml_file='C:/Users/user/Desktop/Minor Project/My things/xml file/haarcascade_eye.xml'
eye_cascade=cv2.CascadeClassifier(eye_xml_file)

cap=cv2.VideoCapture('facemovement.mp4')

while True:
	ret, img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:#drawing a rectangle
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
		eyes=eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

	cv2.imshow('image',img)

	k=cv2.waitKey(100) & 0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()