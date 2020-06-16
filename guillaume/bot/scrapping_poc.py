import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

def connectTo(url, header = {'User-Agent': 'Mozilla/5.0'}):
    requete = requests.get(url, header)
    goodLink = getLink(thingsToFind[i])
    if (".pdf" in goodLink.attrs["href"].lower()):
        requete.close()
        return goodLink
    elif (goodLink and goodLink != ""):
        requete.close()
        i+=1
        connectTo(goodLink)
    else:
        requete.close()
        print("pas trouvé dans : " + url)

def getLink(thingToFind):
    for selecteur in thingToFind[1]:
        tab = soup.find_all(selecteur)
        for link in tab:
            for mot in thingToFind[0]:
                if (mot in link.text.lower()):
                    return link
                else:
                    continue
    
    return ""



urls = ["liste des urls à tester"]
thingsToFind = [[["mots à chercher"], ['sélecteurs']], [["mots à chercher"], ['sélecteurs']], [["mots à chercher"], ['sélecteurs']]]
urlToPdf = []

for url in urls:
    urlToPdf.append(connectTo(url))