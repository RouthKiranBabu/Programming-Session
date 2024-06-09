from PIL import Image,ImageFilter
import os

image1=Image.open('a.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('gassblur.jpg')