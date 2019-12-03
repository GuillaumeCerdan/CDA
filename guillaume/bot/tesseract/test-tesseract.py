import pytesseract
from PIL import Image
from pdf2jpg import pdf2jpg

# Refacto avec format
# Rajouter dans le readme les pip

inputpath = r"raa-cut.pdf"

outputpath = r"folder/"

result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="1")
print("result : " + str(result[0].get("output_jpgfiles")[0]))
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
print(pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0]))))