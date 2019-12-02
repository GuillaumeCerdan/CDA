import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time


# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = "https://www.montblancnaturalresort.com/fr/domaine-skiable-grands-montets"


try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    print("erreur de connection 1")

time.sleep(3)

soup = BeautifulSoup(page, "html.parser")
time.sleep(3)
remontees_ouvertes = soup.find("body")
# pistes_ouvertes = soup.find_all(".infos .col-md-6:last-child > h2 > b")

print(remontees_ouvertes)
# print(pistes_ouvertes)