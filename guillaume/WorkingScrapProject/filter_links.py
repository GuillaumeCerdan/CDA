# -*- coding: utf-8 -*-

import os
import fitz
import sys

from components.PdfHandler import PdfHandler

ph = PdfHandler()

good_ones = set()

# Parcoure les fichiers dans pdf-ardeche
for file in os.listdir("pdf-ardeche"):

    matching_pages = ph.get_matching_pages('pdf-ardeche/' + file)
    if (matching_pages != []):
        print('match : {}'.format(file))
        good_ones.add(file)

    
# Déplace les fichiers
try:
    for one in good_ones:
        os.replace("C:/wamp64/www/WorkingScrapProject/pdf-ardeche/" + one, "C:/wamp64/www/WorkingScrapProject/good-pdfs/" + one)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



# Vide le fichier
file_to_add = open('data-txt/links_to_add.txt', 'w+')
file_to_add.write('')
file_to_add.close()