import numpy as np 
import cv2

img=cv2.imread('thor.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(150,0),(150,150),(0,0,255),15)#creats a line
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)#makes not the border but fills the color
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)#points for drawing polylines
cv2.polylines(img,[pts],True,(0,255,255),3)#True represents wether the final line is 
#to be connected to the first or not

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Opencv Text',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()