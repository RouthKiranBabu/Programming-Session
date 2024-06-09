import numpy as np
import cv2

import pyscreenshot as screen

while True:#for infinite loop
	img=screen.grab()#grab the screen
	img_np=np.array(img)#Converting image into an array
	cv2.imshow("Screen",img_np)#Command for displaying
	if cv2.waitkey(1)==27:
		break

cv2.destroyAllWindows()
#but colour is inverted which is in bgr format while grab command usage but not in rgb 
#format 
