import cv2

print(cv2.haarcascades)
print(cv2.importlib)

face_identifier="C:/Users/user/Desktop/Minor Project/My things/xml file/haarcascade_frontalface_default.xml"
eye_identifier="C:/Users/user/Desktop/Minor Project/My things/xml file/haarcascade_eye.xml"

face_cascade=cv2.CascadeClassifier(face_identifier)
eye_cascade=cv2.CascadeClassifier(eye_identifier)

capture=cv2.VideoCapture("C:/Users/user/Desktop/Minor Project/0. Test/facemovement.mp4")

while True:
	ret, img=capture.read()

	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face=face_cascade.detectMultiScale(gray,1.5,5)

	for (x,y,w,h) in face:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),10)
		cv2.putText(img,"Face found!",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,
			(200,255,255),2,cv2.LINE_AA)

		gray_eye=gray[y:y+h,x:x+w]
		img_eye=img[y:y+h,x:x+w]
		eye=eye_cascade.detectMultiScale(gray_eye)

		for (ex,ey,ew,eh) in eye:
			cv2.rectangle(img_eye,(ex,ey),(ex+ew,ey+eh),(22,0,0),10)
			#cv2.putText(img,"Eye found!",(ex+x,ey+y),cv2.FONT_HERSHEY_SIMPLEX,0.5,
				#(200,255,255),1,cv2.LINE_AA)
			cv2.putText(img_eye,"Eye found!",(ex,ey),cv2.FONT_HERSHEY_SIMPLEX,0.5,
				(200,255,255),1,cv2.LINE_AA)

	cv2.imshow("image capture",img)

	k=cv2.waitKey(100) & 0xff

	if k==27:
		break 

capture.release()
cv2.destroyAllWindows()

