import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

listurl = ["http://www.alpes-de-haute-provence.gouv.fr/", "http://www.bouches-du-rhone.gouv.fr/", "http://www.var.gouv.fr/", "http://www.vaucluse.gouv.fr/", "http://www.alpes-maritimes.gouv.fr/", "http://www.hautes-alpes.gouv.fr/"]

good_url_raa = []

for url in listurl:

    already_passed = False

    print("Le site scrappé : " + url)

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

        if (not already_passed):

            formatted_link_name = link.text.lower()
            formatted_link = link.get("href")

            if "raa" in formatted_link_name and ("recueil" in formatted_link_name or "archives" in formatted_link_name):
                print("Lien publications : " + str(link.get("href")))
                already_passed = True
                if (formatted_link[0] == "/"):
                    good_url_raa.append(url + formatted_link[1:])
                elif (formatted_link[0] == "h"):
                    good_url_raa.append(formatted_link)
                else:
                    good_url_raa.append(url + formatted_link)
    requete.close()
    time.sleep(1)

print (good_url_raa)

for good_url in good_url_raa:
    try:
        requete = requests.get(good_url, headers = header)
        page = requete.content
    except:
        print("erreur de connection 2")
        continue

    soup = BeautifulSoup(page, "html.parser")

    links = soup.find_all("a", href = True)
    list_links = [link.string for link in links]

    for link in list_links:
        #if ("2019" in link.get("href")):
        #print("Lien 2019 : " + link.get("href"))
        print("Lien 2019 : " + link.text)

    requete.close()
    time.sleep(1)