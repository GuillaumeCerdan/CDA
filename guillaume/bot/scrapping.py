import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

fileToSearch = 'departments.csv'
tempFile = open( fileToSearch, 'r' )
listdep = []
listurl = []
for line in fileinput.input(fileToSearch):
    listdep.append(line)
    *_ , ville = line.split(',')
    ville = ville[:-1].replace(' ','-')
    listurl.append(ville.strip('"')+".gouv.fr")

listurl.pop(0)

bads = set()

#Parcours les urls
for url in listurl:
    goodurl = "http://www." + url

    print("Le site scrappé : " + goodurl)

    try:
        requete = requests.get(goodurl, headers = header)
        page = requete.content
    except:
        print("erreur de connection")
        continue


    soup = BeautifulSoup(page, "html.parser")

    links = soup.find_all("a", href = True)
    list_links = [link.string for link in links]

    for link in links:
        # Trouve tous les liens pour les recueils
        if "raa" in link.text.lower() and "recueil" in link.text.lower():
            print("Lien publications : " + str(link.text))
        else:
            bads.add(url + " : " + link.text)

    time.sleep(1)

print(bads)
print(len(bads))