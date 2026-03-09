import pytesseract
from PIL import Image

# If Tesseract is NOT auto-detected, uncomment and edit this line:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Kriti\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open("demo.png")  # image must be in same folder
text = pytesseract.image_to_string(img)

print("----- Extracted Text -----")
print(text)
