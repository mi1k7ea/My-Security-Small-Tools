#!/usr/bin/python
#coding=utf-8
import pytesseract
from PIL import Image

img = Image.open('2.jpg')
result = pytesseract.image_to_string(img)
print result