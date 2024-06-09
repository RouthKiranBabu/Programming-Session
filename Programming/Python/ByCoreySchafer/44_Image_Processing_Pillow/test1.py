#folder containing png file of current jpg file
from PIL import Image
import os

for f in os.listdir('.'):
	if f.endswith('.jpg'):
		print(f)

for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i=Image.open(f)
		fn,fext=os.path.splitext(f)
		
		i.save(f'pngs/{fn}.png')