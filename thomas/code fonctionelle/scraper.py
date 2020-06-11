
from bs4 import BeautifulSoup
import os
import datetime

from PdfHandler import PdfHandler
from ConnectionHandler import ConnectionHandler


f = open("lienCrawler.txt", mode = "r" )
liste_liens = f.read()
liste_liens=set(liste_liens.split('\n'))
f.close()
files = open('lienScrapper.txt', mode = "r")
list_link_used = files.read()
list_link_used = set(list_link_used.split("\n"))
files.close()
link_to_scrap = {link for link in liste_liens if link not in list_link_used}


nb_new_pdfs = 0
new_pdfs = []
files = open('lienScrapper.txt', mode = "a")
for lien in link_to_scrap:

    pdf_url = lien

    page = ConnectionHandler.getPageContent(pdf_url)

    new_link_name = lien.replace('>','')
    
    if (not(PdfHandler.doesPdfExistsAt("pdf-ardeche/" + new_link_name  + ".pdf"))):
        PdfHandler.insertPdfAt("pdf-ardeche/" + new_link_name  + ".pdf", page)
        print("C'est un nouveau RAA")
        nb_new_pdfs += 1
        new_pdfs.append(new_link_name)
    files.write(lien)
    files.write("\n")
    

files.close()
if (nb_new_pdfs > 0):
    if (nb_new_pdfs == 1):
        print("Il y a eu 1 PDF rajouté")
        print("Le voici : {}".format(new_pdfs))
    else:
        print("Il y a eu {} PDFs rajoutés".format(nb_new_pdfs))
        print("Les voici : {}".format(new_pdfs))