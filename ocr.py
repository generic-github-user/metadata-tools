print('Importing libraries...')
from PIL import Image, ImageOps
import pytesseract
import json
#import ImageStat

invert = True

#filename = 'Annotation 2019-10-19 160040.png'
filename = 'testimg1.png'
#filename = 'testimg2.jpg'
#filename = 'testimg3.png'
#filename = 'testimg4.png'
#filename = 'testimg5.png'
filename = 'unknown.png'
print('Analyzing %s...'%filename)
