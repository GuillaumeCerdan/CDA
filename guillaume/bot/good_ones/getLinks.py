import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

# Traite les urls
fileToSearch = 'departments.csv'
tempFile = open( fileToSearch, 'r' )
listdep = []
listurl = []

# Récupère les noms des départements et créé les urls
for line in fileinput.input(fileToSearch):
    listdep.append(line)
    *_ , dep = line.split(',')
    dep = dep[:-1].replace(' ','-')
    listurl.append(dep.strip('"')+".gouv.fr")


# Enlève la première ligne qui n'est pas de la data
listurl.pop(0)


test_url = []

#Parcourt les urls
for url in listurl:
    time.sleep(1)
    goodurl = "http://www." + url

    print("Le site scrappé : " + goodurl)
    val = []
    val.append("Le site scrappé : " + goodurl)

    #Url à parcourir
    # try catch pour verifier si la connection fonctione sinon on passe cette url
    try:
        requete = requests.get(goodurl, headers = header)
        page = requete.content
    except:
        # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
        print("erreur de connection")
        continue


    # Parser html
    soup = BeautifulSoup(page, "html.parser")

    # Tous les liens
    links = soup.find_all("a", href = True)
    titles = soup.find_all("h1")
    spans = soup.find_all("span")

    #mise en place des tableaux avec les liens
    list_links = [link.string for link in links]
    list_titles = [title.string for title in titles]
    list_spans = [span.string for span in spans]

    for link in links:
        if ("/publication" == link.attrs['href'].lower()) or ("/publications" == link.attrs['href'].lower()) :
            test_url.append(goodurl+link.attrs["href"])
            break
        if (("publications-r" in link.attrs['href'].lower()) or("publication-r" in link.attrs['href'].lower())):
            test_url.append(goodurl+"/"+link.attrs["href"])
            break

    # Ecriture dans le fichier donnees.csv
    with open("donnees.csv", "a", newline='', encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(val)
        writer.writerow(list_spans)
        writer.writerow('')

print(test_url)
