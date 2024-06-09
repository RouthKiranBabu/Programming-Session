from PIL import Image 
import os 

imagefile="cheetha.jpg"
createfile='saved file'

saveimageas="newcheetha.jpg"

print(os.listdir())

if createfile not in os.listdir():
	os.mkdir(createfile)

imageval=Image.open(imagefile)

for filename in os.listdir():
	if filename.endswith(".jpg"):
		f, ext= os.path.splitext(filename)
		print(f)
		print(ext)
		imageval.save(f"{createfile}/{saveimageas}")