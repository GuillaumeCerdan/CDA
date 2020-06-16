import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time


# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

url = "http://www.ardeche.gouv.fr/septembre-2019-a8540.html"


try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    print("erreur de connection 1")


soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)
list_links = [link.string for link in links]
i = 0
for link in links:
    # Trouve tous les liens pour les recueils
    if (".pdf" in link.get("href")):
        text_link = link.text
        requete.close()
        pdf_url = 'http://www.ardeche.gouv.fr/' + link.get("href")
        requete = requests.get(pdf_url, headers = header)
        page = requete.content
        open("pdf_ardeche_septembre/" + text_link  + ".pdf", 'wb').write(page)
        i+=1
        time.sleep(1)