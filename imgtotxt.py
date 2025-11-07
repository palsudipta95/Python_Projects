import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert():
    img = Image.open('random1.png')
    text = pytesseract.image_to_string(img)
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(text)

convert()