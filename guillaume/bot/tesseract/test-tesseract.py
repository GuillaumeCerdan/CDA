import pytesseract
from PIL import Image
from pdf2jpg import pdf2jpg
import os
import PyPDF2, io, requests

files = [f for f in os.listdir('.') if os.path.isfile(f)]

#print(files)

for file in files:

    inputpath = file

    response = requests.get("file://C:\wamp64\www\CDA\guillaume\\bot\\tesseract\\" + inputpath)

    outputpath = "folder/"

    num_pages = 0

    with io.BytesIO(response.content) as open_pdf_file:
        read_pdf = PyPDF2.PdfFileReader(open_pdf_file)
        num_pages = read_pdf.getNumPages()

    for num_page in num_pages:

        result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages=str(num_page))

        # print(result)

        # print("result : " + str(result[0].get("output_jpgfiles")[0]))
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
        if ("écologie" in pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0]))).lower() or "ecologie" in pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0]))).lower()):
            print("_" * 40)
            print(inputpath)