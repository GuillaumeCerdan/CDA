import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time


# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

url = "http://www.ardeche.gouv.fr"


try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    print("erreur de connection 1")


soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)
for link in links:
    # Trouve tous les liens pour les recueils
    if ("raa" in link.text.lower()):
        requete.close()
        time.sleep(1)
        requete = requests.get(link.get("href"), headers = header)
        page = requete.content
        print(page)