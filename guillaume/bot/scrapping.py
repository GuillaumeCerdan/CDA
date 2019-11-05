import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0Chrome'}

#Parcours les urls
fileToSearch = 'departments.csv'
tempFile = open( fileToSearch, 'r' )
listdep = []
listurl = []
for line in fileinput.input(fileToSearch):
    listdep.append(line)
    *_ , ville = line.split(',')
    ville = ville[:-1].replace(' ','-')
    listurl.append(ville.strip('"')+".gouv.fr")


for url in listurl:

    goodurl = "http://www.quevisiter.fr"

    #requete = requests.get(goodurl, headers = header)
    requete = requests.get(goodurl, allow_redirects=True)

    if requete.history:
        print("redirigé")

    try:
        print(requete.content)

    except:
        print("Chais pas")

    # with open("donneesrobots.csv", "a", newline='', encoding="utf-8") as fichier:
    #     writer = csv.writer(fichier)
    #     for i in range(j):
    #         writer.writerow(list_pre)
    #         writer.writerow([30 * "_"])

    time.sleep(1)
