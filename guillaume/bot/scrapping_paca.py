import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

def formatUrl(original_link, link_raa):
    # Si lien relatif 
    if link_raa[0] == "/":
        return original_link + newurl[1:]
    # Lien ok
    elif link_raa[0] == "h":
        return link_raa
    # Lien relatif sans le "/"
    else:
        return original_link + newurl

# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

listurl = ["http://www.var.gouv.fr/", "http://www.vaucluse.gouv.fr/", "http://www.alpes-maritimes.gouv.fr/", "http://www.alpes-de-haute-provence.gouv.fr/", "http://www.hautes-alpes.gouv.fr/", "http://www.bouches-du-rhone.gouv.fr/"]

#Parcours les urls
for url in listurl:

    #print("Le site scrappé : " + url)

    try:
        requete = requests.get(url, headers = header)
        page = requete.content
    except:
        print("erreur de connection 1")
        continue


    soup = BeautifulSoup(page, "html.parser")

    links = soup.find_all("a", href = True)
    list_links = [link.string for link in links]

    for link in links:
        # Trouve tous les liens pour les recueils
        if ("raa" in link.text.lower() and "recueil" in link.text.lower()) or "raa et archives" in link.text.lower():
            newurl = link.get('href')
            newurl = formatUrl(url, newurl)
            print(newurl)


    time.sleep(1)

    requete.close()

    try:
        requete = requests.get(newurl, headers = header)
        page = requete.content
    except:
        print("erreur de connection 2")
        continue


    soup = BeautifulSoup(page, "html.parser")

    newlinks = soup.find_all("a", href = True)

    #for newlink in newlinks:
        #print(newlink.prettify())

    





