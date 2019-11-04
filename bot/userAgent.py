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

time.sleep(1)

goodurl = "http://www.quevisiter.fr"

#requete = requests.get(goodurl, headers = header)
requete = requests.get(goodurl)

try:
    print(requete.content)

except:
    print("Chais pas")

# with open("donneesrobots.csv", "a", newline='', encoding="utf-8") as fichier:
#     writer = csv.writer(fichier)
#     for i in range(j):
#         writer.writerow(list_pre)
#         writer.writerow([30 * "_"])
