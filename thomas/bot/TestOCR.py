import pytesseract
from PIL import Image
from pdf2jpg import pdf2jpg
import os


path = 'D:\\projet\\github\\CDA\\thomas\\bot'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

# for f in files:
#     print(f)

# Refacto avec format
# Rajouter dans le readme les pip
retourtext = open("test.txt","a")
# inputpath = r"RAA-test.pdf"
pytesseract.pytesseract.tesseract_cmd = r"D:/programme/Tesseract-OCR/tesseract.exe"

outputpath = r"temp/"

# result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300)#on garde les 300 dpi pour avoir une meilleur qualité 
# # print(str(result))
# #print("result : " + str(result[0].get("output_jpgfiles")[0]))
# pytesseract.pytesseract.tesseract_cmd = r"D:/programme/Tesseract-OCR/tesseract.exe"
# # print(str(result[0].get("output_jpgfiles")[0]))
# texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0])))
# print(texteImg)
# retourtext = open(r"test.txt","a")
# retourtext.write(texteImg)
# retourtext.close()
# # print("coucou")
# os.startfile("test.txt")

for file in files :
    inputpath = file
    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300)#on garde les 300 dpi pour avoir une meilleur qualité 
    print(str(result))
    # print("result : " + str(result[0].get("output_jpgfiles")))
    # print(str(result[0].get("output_jpgfiles")[0]))
    texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0])))
    # print(texteImg)
    retourtext = open(r"test.txt","a")
    retourtext.write(texteImg)
retourtext.close()
os.startfile("test.txt")
