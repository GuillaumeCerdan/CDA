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
for line in fileinput.input(fileToSearch):
    listdep.append(line)
    *_ , ville = line.split(',')
    ville = ville[:-1].replace(' ','-')
    listurl.append(ville.strip('"')+".gouv.fr")
    

listurl.pop(0)
print (listurl)

#Parcours les urls
for url in listurl:

    time.sleep(1)

    goodurl = "http://www." + url + "/robots.txt"

    #Url à parcourir
    requete = requests.get(goodurl, headers = header)

    try:
        print(requete.status_code)
        if (requete.status_code == 200):
            print("Robots.txt - " + url + " opérationnel")
        else:
            print("XXXXXXX Robots.txt - " + url + " non opérationnel")

    except:
        print("Une erreur est survenue")
