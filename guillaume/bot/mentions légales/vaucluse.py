import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

url = "http://www.vaucluse.gouv.fr/"

try:
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

requete.close()
time.sleep(2)

try:
    requete = requests.get(url + urlmentionlegales, headers = header)
    page = requete.content
    soup = BeautifulSoup(page, "html.parser")
except Exception as e:
    print(e)

html = soup.prettify()

# Ecriture dans le fichier donnees.csv
with open("vaucluse.html", "a", newline='', encoding="utf-8") as fichier:
    fichier.write(html)