
############## PART 1: Using pytesseract.image_to_string() for text extraction

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open('C:/Users/vishal.gupta33/Desktop/imageToText/atm_thumb_01.jpg')

#Image Preprosessing/Enhancement

# Convert into Monochromatic image
im = im.convert('L')   

# Streched the image along width
w, h = im.size
im=im.resize ( (w*5, int(h*4.25)) , Image.ANTIALIAS )   

# Experimented with Contrast, Sharpness and Brightness
contrast = ImageEnhance.Contrast(im)
im = contrast.enhance(2)

sharpness = ImageEnhance.Sharpness(im)
im = sharpness.enhance(5)

brightness = ImageEnhance.Brightness(im)
im = brightness.enhance(0.4)

# Extracting text
text = pytesseract.image_to_string(im)
print (text)


############## PART 2: Getting bounding box coordinates using hOCR

from pytesseract import pytesseract

pytesseract.run_tesseract('C:\\Users\\vishal.gupta33\\Desktop\\imageToText\\test2.png', 
                          'output', 
                          lang=None, boxes=False,  config="hocr")

#creates an output.html file with bounding box coordinates
#Note: I don't know how I would use these coordinates to form an editable text yet.
