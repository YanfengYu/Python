import pytesseract as py
from PIL import Image

image = Image.open(r'C:\Users\pc\Desktop\4.jpg')

text = py.image_to_string(image)
print(text)
