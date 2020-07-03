from bs4 import BeautifulSoup
import os
import datetime

from FileHandler import FileHandler
from ConnectionHandler import ConnectionHandler
from LoggerHandler import LogHandler 

dossier_pdf = "pdf-ardeche/"
#  use with 
with open("lienCrawler.txt", mode = "r+"  ,encoding='UTF-8') as f: 
    liste_liens = f.read()
    liste_liens = set(liste_liens.split('\n'))

with open('lienScrapper.txt', mode = "r+", encoding='UTF-8') as f:
    list_link_used = f.read()
    list_link_used = set(list_link_used.split("\n"))
link_to_scrap = {link for link in liste_liens if link not in list_link_used}


nb_new_pdfs = 0
new_pdfs = []

with open('lienScrapper.txt', mode = "a", encoding='UTF-8') as files:
    for lien in link_to_scrap:


        page = ConnectionHandler.get_page_content(lien)


        file_name = ConnectionHandler.get_name_PDF(lien)

        
        if not FileHandler.is_exist_file(dossier_pdf + file_name):
            if FileHandler.insert_file(dossier_pdf + file_name, page):
                nb_new_pdfs += 1
                files.write(lien)
                files.write("\n")

LogHandler.logger_info(f"{LogHandler.get_date()}  {nb_new_pdfs} téléchargements")