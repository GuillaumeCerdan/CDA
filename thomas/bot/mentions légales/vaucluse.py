import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

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
# print(listurl)

# url = "http://www.vaucluse.gouv.fr/"

# try:
#     requete = requests.get(url, headers = header)
#     page = requete.content
# except:
#     print("erreur de connection")


# soup = BeautifulSoup(page, "html.parser")

# links = soup.find_all("a", href = True)

# list_links = [link.string for link in links]

# for link in links:
#     if "mentions légales" in link.text.lower():
#         urlmentionlegales = link.get('href')

# requete.close()
# time.sleep(2)

# try:
#     requete = requests.get(url + urlmentionlegales, headers = header)
#     page = requete.content
#     soup = BeautifulSoup(page, "html.parser")
# except Exception as e:
#     print(e)

# html = soup.prettify()

# # Ecriture dans le fichier donnees.csv
# with open("vaucluse.html", "a", newline='', encoding="utf-8") as fichier:
#     fichier.write(html)

for url in listurl:
    urlenrg  = url
    url = "http://www." + url
    try:
        # print(url)
        requete = requests.get(url, headers = header)
        page = requete.content
    except:
        print("erreur de connection")


    soup = BeautifulSoup(page, "html.parser")

    links = soup.find_all("a", href = True)

    list_links = [link.string for link in links]

    for link in links:
        if "mentions légales" in link.text.lower():
            urlmentionlegales = link.get('href')
            if not ("http" in urlmentionlegales):
                urlmentionlegales = url + "/" + urlmentionlegales
            else :
                urlmentionlegales = url + urlmentionlegales

    requete.close()
    time.sleep(1)
    print(urlmentionlegales)
    try:
        requete = requests.get(urlmentionlegales, headers = header)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")
    except Exception as e:
        print(e)

    html = soup.prettify()

    # Ecriture dans le fichier donnees.csv
    with open(urlenrg + ".html", "a", newline='', encoding="utf-8") as fichier:
        fichier.write(html)

    requete.close()
    
