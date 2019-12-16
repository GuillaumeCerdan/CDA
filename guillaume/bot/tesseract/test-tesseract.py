import pytesseract
from PIL import Image
from pdf2jpg import pdf2jpg
import os
import pyPdf

files = [f for f in os.listdir('.') if os.path.isfile(f)]

#print(files)

for file in files:

    inputpath = file

    outputpath = "folder/"

    reader = pyPdf.PdfFileReader(open("foo.pdf"))
    print reader.getNumPages()

    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="1")

    # print(result)

    # print("result : " + str(result[0].get("output_jpgfiles")[0]))
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
    if ("écologie" in pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0]))).lower() or "ecologie" in pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0]))).lower()):
        print("_" * 40)
        print(inputpath)