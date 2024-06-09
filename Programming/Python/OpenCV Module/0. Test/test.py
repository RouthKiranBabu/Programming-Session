import cv2

face_identifier="C:/Users/user/Desktop/Minor Project/My things/xml file/haarcascade_frontalface_default.xml"
eye_identifier="C:/Users/user/Desktop/Minor Project/My things/xml file/haarcascade_eye.xml"

face_cascade=cv2.CascadeClassifier(face_identifier)
eye_cascade=cv2.CascadeClassifier(eye_identifier)

capture=cv2.VideoCapture("facemovement.mp4")

while True:
	ret, face_image=capture.read()
	face_gray=cv2.cvtColor(face_image,cv2.COLOR_BGR2GRAY)
	face=face_cascade.detectMultiScale(face_gray,1.3,5)
	for (fx,fy,fw,fh) in face:
		cv2.rectangle(face_image,(fx,fy),(fx+fw,fy+fh),(0,200,0),2)
		cv2.putText(face_image,"Face found!",(fx,fy),2,cv2.FONT_HERSHEY_SIMPLEX,(220,0,0),1,cv2.LINE_AA)

		eye_gray=face_gray[fy:fy+fh,fx:fx+fw]
		eye_image=face_image[fy:fy+fh,fx:fx+fw]
		eye=eye_cascade.detectMultiScale(eye_gray)

		for (ex,ey,ew,eh) in eye:
			cv2.rectangle(eye_image,(ex,ey),(ex+ew,ey+eh),2)

	cv2.imshow("Image detection",face_image)

	key=cv2.waitKey(100) & 0xff

	if key==27:
		break 

capture.release()
cv2.destroyAllWindows()