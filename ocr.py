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

img = Image.open(filename)
img = img.convert('RGB')
#blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')

#stat = ImageStat.Stat(im)
#avg = stat.mean[0]

def brightness(image):
	grayscale = image.convert('L')
	histogram = grayscale.histogram()
	pixels = sum(histogram)
	b = scale = len(histogram)
	
	for index in range (0, scale):
		ratio = histogram[index] / pixels
		b += ratio * (-scale + index)
		
	return b / scale

print('Brightness averages %s across image'%brightness(img))
lightness = brightness(img)
#img = img.point(lambda x: 0 if x < 200 else 255, '1')

if lightness < 0.5 and invert:
	print('Inverting image before processing...')
	img = ImageOps.invert(img)
	
print('Detected text: \n')
text = pytesseract.image_to_string(img);

#boxes = pytesseract.image_to_boxes(Image.open(filename));
#data = pytesseract.image_to_data(Image.open(filename), output_type=pytesseract.Output.DICT);
#data = json.dumps(data, indent='\t')

print(text)