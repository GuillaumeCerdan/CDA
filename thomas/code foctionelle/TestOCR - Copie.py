import pytesseract
from PIL import Image
from pdf2jpg import pdf2jpg
from datetime import date
import os


path = 'D:\\projet\\github\\CDA\\thomas\\bot'
# fichier pdf 
inputpath = r"test.pdf"
# lien ver tesseract
pytesseract.pytesseract.tesseract_cmd = r"D:/programme/Tesseract-OCR/tesseract.exe"
# dossier d'output pour les image
outputpath = r"temp/"

#création de l'objet resultat (dans l'objet resultat il faut get 'output_jpgfiles')
#on boucle sur toutes les image former par l'objet resultat 
result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="ALL") #on garde les 300 dpi pour avoir une meilleur qualité 

# lecture du texte dans l'image
texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0])),lang='fra')
# ecriture dans un fichier 
retourtext = open(r"test.txt","a")
retourtext.write('£££ lu avec tesseract le {} \n'.format(date.today()))
retourtext.write(texteImg.strip())
# boucle sur tout les fichier
for i in range (0, len(result[0].get("output_jpgfiles"))):
    texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[i])))
    retourtext.write(texteImg.strip()) 
retourtext.close()

os.startfile("test.txt")


def readerPDFImg(inputPath,output = r"temp" ):
    pytesseract.pytesseract.tesseract_cmd = r"D:/programme/Tesseract-OCR/tesseract.exe"

    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="ALL") #on garde les 300 dpi pour avoir une meilleur qualité 

    # lecture du texte dans l'image
    texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0])),lang='fra')

    retourtext = '£££ lu avec tesseract le {} \n'.format(date.today())
    retourtext += texteImg.strip()
    # boucle sur tout les fichier
    for i in range (0, len(result[0].get("output_jpgfiles"))):
        texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[i])),lang='fra')
        retourtext+= texteImg.strip()