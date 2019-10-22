import os
import csv
import requests
from bs4 import BeautifulSoup


requete = requests.get("https://www.getup.agency")
page = requete.content
soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a")

list_links = [links.string.strip() for link in links]


print(list_links)