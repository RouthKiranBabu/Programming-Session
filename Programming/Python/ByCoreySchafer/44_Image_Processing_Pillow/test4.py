from PIL import Image
import os

image1=Image.open('a.jpg')
image1.rotate(90).save('rot90.jpg')