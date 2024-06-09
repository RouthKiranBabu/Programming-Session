#300 folder containing 300px size

size_300=(300,300)
size_700=(700,700)

from PIL import Image
import os

for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i=Image.open(f)
		fn,fext=os.path.splitext(f)
		i.thumbnail(size_700)
		i.save(f'700/{fn}_700{fext}')

		i.thumbnail(size_300)
		i.save(f'300/{fn}_300{fext}')