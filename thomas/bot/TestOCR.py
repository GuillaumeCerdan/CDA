from PIL import Image
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core('placeholder.png'))