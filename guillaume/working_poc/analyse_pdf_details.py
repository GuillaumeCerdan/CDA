from PyPDF2 import PdfFileReader
import os
from pdf2jpg import pdf2jpg
import fitz


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



# # Convertit un pdf en image
# def pdf_to_img(pdf_file, index):
#     return pdf2jpg.convert_pdf2jpg(pdf_file, "pdf-ardeche-img/", dpi=300, pages=str(index))


# # Retourne le texte détecté sur l'image
# def ocr_core(file):
#     text = pytesseract.image_to_string(file)
#     return text


# def print_page_at_index(pdf_file, index):
#     images = pdf_to_img(pdf_file, index)
#     print(images[0])
#     return ocr_core(images)
#     # for img, idx in enumerate(images):
#     #     if (idx == index):
#     #         return ocr_core(img)



# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

reader = PdfFileReader(open('pdf-ardeche/recueil_raa_no07-2020-039-du_14_mai_2020-special_1_.pdf', 'rb'))

# print(reader.getOutlines())

for x in range(reader.numPages):
    page = reader.getPage(x).extractText()

    # print(page)
    # print("")
    # print(x)
    # print("")
    # print("")
    # print("-------------")
    # print("")


# FITZ IMAGES

# doc = fitz.open("pdf-ardeche/test2.pdf")
# for i in range(len(doc)):
#     for img in doc.getPageImageList(i):
#         xref = img[0]
#         pix = fitz.Pixmap(doc, xref)

#         # Si l'image est grise ou en RGB
#         if pix.n < 5:
#             if (pix.width > 2000):
#                 print("pixMap.width : {}".format(pix.width))
#                 print("pixMap.height : {}".format(pix.height))
#                 print("C'est une page entière scannée")
#                 pix.writePNG("p%s-%s.png" % (i, xref))
#         # Convertit en RGB d'abord
#         else:
#             if (pix.width > 2000):
#                 print("pixMap.width : {}".format(pix.width))
#                 print("pixMap.height : {}".format(pix.height))
#                 print("C'est une page entière scannée")
#                 pix1 = fitz.Pixmap(fitz.csRGB, pix)
#                 # pix1.writePNG("p%s-%s.png" % (i, xref))
#             pix1 = None
#         pix = None


# 314 est une valeur prise sur une page de pdf avec des phrase s mais la page n'était pas remplie
    # if (len(page) < 314):
    #     print("ça pourrait être une image, il y a {} mots à la page n°{}".format(len(page), x + 1))

    #     len_from_tess = print_page_at_index('pdf-ardeche/test2.pdf', x)

    #     print("Tesseract détecte {} mots dans cette page".format(len_from_tess))



    # else:
    #     print("celle ci devrait être une vraie page, il y a {} mots à la page n°{}".format(len(page), x + 1))



#print(pytesseract.image_to_string(Image.open('C:\wamp64\www\CDA\guillaume\ocr\c.png')))




# Bouche du rhône et Ardèche ont des table of content mais PDFMiner et PyPDF2 ne le détectent pas...
# Alors que test-pdf.pdf on les voit bien
# Si on détecte du texte en particulier

# essayer de détecter les éléments Images dans les pdfs via PyPDF2 et donc envoyer que les grandes à Tesseract
# possibilité d'extraire les getTextBlocks via PyPDF2