
from bs4 import BeautifulSoup
import os
import datetime

from PdfHandler import PdfHandler
from ConnectionHandler import ConnectionHandler
from LoggerHandler import LogHandler 

dossier_pdf = "pdf-ardeche/"
#  use with 
with open("lienCrawler.txt", mode = "r"  ,encoding='UTF-8') as f 
    liste_liens = f.read()
    liste_liens=set(liste_liens.split('\n'))

with open('lienScrapper.txt', mode = "r", encoding='UTF-8') as f
    list_link_used = f.read()
    list_link_used = set(list_link_used.split("\n"))
link_to_scrap = {link for link in liste_liens if link not in list_link_used}


nb_new_pdfs = 0
new_pdfs = []
# with open
with open('lienScrapper.txt', mode = "a", encoding='UTF-8') as files
    for lien in link_to_scrap:

        pdf_url = lien

        page = ConnectionHandler.getPageContent(pdf_url)

        # new_link_name = lien.replace('>','')
        # new_link_name = new_link_name.split('/')
        # file_name  = new_link_name[-1]
        file_name = ConnectionHandler.get_name_PDF(lien)

        
        if (not(PdfHandler.doesPdfExistsAt(dossier_pdf +file_name))):
            if PdfHandler.insertPdfAt(dossier_pdf +file_name, page):
                nb_new_pdfs += 1
                files.write(lien)
                files.write("\n")
        


LogHandler.logger_info(f"il y a eu {nb_new_pdfs} telechargement le {LogHandler.get_date()}")