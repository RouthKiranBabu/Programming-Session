#making jpg into png
from PIL import Image
image1=Image.open('a.jpg')
image1.save('newlycreatedbyPython.jpg')

'''
with Image.open('cheetha.jpg') as image:
	image.save('newlycreatedbyPython.jpg')'''