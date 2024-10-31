import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Полный путь к tesseract

img = Image.open('phone_number.png')

text = pytesseract.image_to_string(img)
print(text)
