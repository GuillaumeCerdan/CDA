import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time


# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = "http://www.bouches-du-rhone.gouv.fr/Publications/RAA-et-Archives/Archives-RAA-des-Bouches-du-Rhone/RAA-2019"


try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    print("erreur de connection 1")


soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)
list_links = [link.string for link in links]

bad_links = []

for link in links:

    # Trouve tous les liens pour les recueils
    if (".pdf" in link.get("href")):
        text_link = link.get("href").split("/")[-1].replace(" ", "-")
        print(text_link)
        requete.close()
        pdf_url = 'http://www.bouches-du-rhone.gouv.fr' + link.get("href")
        print(pdf_url)
        print("_" * 20)
        time.sleep(2)
        requete = requests.get(pdf_url, headers = header)
        if (requete.status_code != 200):
            print("Erreur : {}".format(requete.status_code))
            requete.close()
            print("Retry...")
            requete = requests.get(pdf_url, headers = header)
            time.sleep(7)
            page = requete.content
            if (requete.status_code != 200):
                print("{} qui ne marche pas...".format(text_link))
                bad_links.append(text_link)
            else:
                open("bouches_du_rhone_2019/pdf_" + text_link, 'wb').write(page)
                requete.close()
        else:
            page = requete.content
            open("bouches_du_rhone_2019/pdf_" + text_link, 'wb').write(page)
            time.sleep(2)
            requete.close()

if (bad_links):
    print("Nombre de mauvais liens : {}".format(len(bad_links)))
    print(bad_links)
