# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
from sys import argv
import os

from PdfHandler import PdfHandler
from ConnectionHandler import ConnectionHandler

import argparse



# Date Handler
list_mois = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

date_now = datetime.datetime.now()

if (argv[-1] in list_mois):
    month = argv[-1]
else:
    month = list_mois[date_now.date().month - 1]

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))

year = date_now.date().year

page = ConnectionHandler.fetchRessource()
soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)

print("Connecté à la liste des liste des RAA du mois de {}".format(month))

list_links = [link.attrs['href'] for link in links if link.string == "{} {}".format(month,year)]
url = list_links[0]

urls_raa = ConnectionHandler.fetchRessourcesLinks('http://www.ardeche.gouv.fr/' + url)


# Rediriger le stdout du premier script vers le stdin du second script


















# page = ConnectionHandler.fetchRessource('http://www.ardeche.gouv.fr/' + url)

# soup = BeautifulSoup(page, "html.parser")


# links = soup.find_all("a", href = True)
# liste_lien = [link for link in links if "raa" in link.attrs['href'] and "pdf" in link.attrs['href'] ]

# nb_new_pdfs = 0
# new_pdfs = []

# for lien in liste_lien:

#     pdf_url = 'http://www.ardeche.gouv.fr/' + lien.attrs["href"]

#     # On le télécharge même si on l'a déjà
#     page = ConnectionHandler.fetchRessource(pdf_url)

#     new_link_name = lien.text.replace('>','')

#     pdf_location = "pdf-ardeche/" + new_link_name  + ".pdf"
#     pdf_text_location = "pdf-ardeche-text/" + new_link_name  + ".txt"
    
#     if (not(PdfHandler.doesPdfExistsAt(pdf_location))):
#         PdfHandler.insertPdfAt(pdf_location, page)
#         print("C'est un nouveau RAA")
#         nb_new_pdfs += 1
#         new_pdfs.append(new_link_name)
#         PdfHandler.insertPdfTextAt(pdf_location, pdf_text_location)


# if (nb_new_pdfs > 0):
#     if (nb_new_pdfs == 1):
#         print("Il y a eu 1 PDF rajouté")
#         print("Le voici : {}".format(new_pdfs))
#     else:
#         print("Il y a eu {} PDFs rajoutés".format(nb_new_pdfs))
#         print("Les voici : {}".format(new_pdfs))

#f = open("")


# Mettre en place des fcts
# Bien séparer le crawler et le scrapper
# Implémenter le nombre de retry

# Sélecteur vers la table qui contient tous les pdf :
# //*[@id="main"]/div[3]/div[2]/div[3]

# Mettre en place la doc des fonctions et des classes

# Les etags (à regarder)