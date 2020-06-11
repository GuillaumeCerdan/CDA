# -*- coding: utf-8 -*-

from PdfHandler import PdfHandler
from ConnectionHandler import ConnectionHandler

from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )

link_to_fetch = open('links_to_add.txt', "r+", encoding="utf-8")
lines_in_file = link_to_fetch.readlines() 

for line in lines_in_file:
    formatted_line = line.replace("\n", "")
    pdf = ConnectionHandler.fetchRessource(retry_strategy, formatted_line)
    new_link_name = formatted_line.split("pdf/")[1].split('.pdf')[0]
    pdf_location = "pdf-ardeche/" + new_link_name  + ".pdf"

    PdfHandler.insertPdfAt(pdf_location, pdf)

# Vide le fichier links_to_add.txt
# link_to_fetch.seek(0)
# link_to_fetch.write("")
# link_to_fetch.truncate()
link_to_fetch.close()
