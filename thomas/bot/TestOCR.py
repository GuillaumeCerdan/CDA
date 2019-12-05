from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path(r'test.pdf', 500)


