# -*- coding: utf-8 -*-

from components.PdfHandler import PdfHandler
from components.ConnectionHandler import ConnectionHandler

from requests.packages.urllib3.util.retry import Retry

ph = PdfHandler()

retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )

# Récupère tous les nouveaux RAA
link_to_fetch = open('data-txt/links_to_add.txt', "r+", encoding="utf-8")
lines_in_file = link_to_fetch.readlines() 

# Les parcourt
for line in lines_in_file:

    formatted_line = line.replace("\n", "")
    
    # S'y connecte
    pdf = ConnectionHandler.fetch_ressource(retry_strategy, formatted_line)
    new_link_name = formatted_line.split("pdf/")[1].split('.pdf')[0]
    pdf_location = "pdf-ardeche/" + new_link_name  + ".pdf"

    # Les télécharge
    ph.insert_pdf_at(pdf_location, pdf)
    print("Le pdf {} a été téléchargé".format(new_link_name + ".pdf"))

# Ferme la connection
link_to_fetch.close()