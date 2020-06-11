import PyPDF2
import os
import fitz

from components.PdfHandler import PdfHandler

config = ["pollution", "particule fine", "changement climatique", "OGM", "déchets", "empreinte écologique", "a"]

good_ones = set()

# Parcoure les fichiers dans pdf-ardeche
for file in os.listdir("pdf-ardeche"):

    pdfFileObj = open('pdf-ardeche/' + file, 'rb')
    
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages

    # Pour chaque page du RAA
    for x in range(numPages):

        page = pdfReader.getPage(x).extractText()

        if (len(page) < 150) :
            pass
            # Sinon c'est que c'est soit une image soit un titre/première page

        # Si mot dans page
        for item in config:
            if (item in page):
                # Ajoute dans une liste les RAA qui matchent
                good_ones.add(file)

    pdfFileObj.close()

# Déplace les fichiers
try:
    for one in good_ones:
        os.replace("C:/wamp64/www/WorkingScrapProject/pdf-ardeche/" + one, "C:/wamp64/www/WorkingScrapProject/good-pdfs/" + one)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



# Vide le fichier
file_to_add = open('data-txt/links_to_add', 'w+')
file_to_add.write('')
file_to_add.close()