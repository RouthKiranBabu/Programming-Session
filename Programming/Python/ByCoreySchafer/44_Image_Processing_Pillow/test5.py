from PIL import Image
import os

image1=Image.open('a.jpg')
image1.convert(mode='L').save('modeL.jpg')