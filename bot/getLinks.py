import os
import csv
import requests
from bs4 import BeautifulSoup

#Url à parcourir
requete = requests.get("https://www.getup.agency")
page = requete.content

# Parser html
soup = BeautifulSoup(page, "html.parser")

#Tous les liens
links = soup.find_all("a")

list_links = [link.string for link in links]

# Les print
for link in list_links :
    print(link)
