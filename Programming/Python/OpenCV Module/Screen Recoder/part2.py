import numpy as np
import cv2

import pyscreenshot as screen

def func():
	while True:
		img=screen.grab()
		img_np=np.array(img)

		frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
		cv2.imshow("Screen",frame)
		if cv2.waitKey(1)==27:
			break
cv2.destroyAllWindows()

if __name__ == '__main__':
	func()