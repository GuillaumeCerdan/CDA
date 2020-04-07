import pdf2image
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for img in enumerate(images):
        print(ocr_core(img))

print_pages(pdf_to_img('raa_no07-2020-012_du11022020-special.pdf'))
# if ("installations classées" in pdf_to_img('raa_no07-2020-012_du11022020-special.pdf')):
#     print('il y est !')