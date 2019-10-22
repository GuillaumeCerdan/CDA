import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup

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
print (listurl)


for url in listurl:

    goodurl = "http://www." + url

    print("Le site scrappé : " + goodurl)

    #Url à parcourir
    requete = requests.get(goodurl, headers = header)
    page = requete.content

    # Parser html
    soup = BeautifulSoup(page, "html.parser")

    # Tous les liens
    links = soup.find_all("a")
    titles = soup.find_all("h1")

    #list_links = [link.string for link in links]
    list_titles = [title.string for title in titles]

    print(list_titles)

    # Ecriture
    j = len(list_titles)
    i = 0
    with open("donnees.csv", "w", newline='', encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        while i < j:
            if (list_titles[i] != ""):
                writer.writerow(str(list_titles[i]))
            i+=1
