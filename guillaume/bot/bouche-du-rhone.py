import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = "http://www.bouches-du-rhone.gouv.fr/"

good_url_raa = []

already_passed = False

print("Le site scrappé : " + url)

try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    print("erreur de connection 1")


soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)
list_links = [link.string for link in links]

for link in links:

    if (not already_passed):

        formatted_link_name = link.text.lower()
        formatted_link = link.get("href")

        if "raa" in formatted_link_name and ("recueil" in formatted_link_name or "archives" in formatted_link_name):
            print("Lien publications : " + str(link.get("href")))
            already_passed = True
            if (formatted_link[0] == "/"):
                good_url_raa.append(url + formatted_link[1:])
            elif (formatted_link[0] == "h"):
                good_url_raa.append(formatted_link)
            else:
                good_url_raa.append(url + formatted_link)

requete.close()

print (good_url_raa)


try:
    requete = requests.get(good_url_raa[0], headers = header)
    page = requete.content
except:
    print("erreur de connection 2")

soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)
# list_links = [link.string for link in links]

# for link in list_links:
#     #if ("2019" in link.get("href")):
#     #print("Lien 2019 : " + link.get("href"))
#     print("Lien 2019 : " + link.text)

publications = ""

for link in links:
    if ("2019" in link.get("href")):
        print(link.get("href"))
        if (link[0] == "/"):
            publications = (url + link.get("href")[1:])
        elif (link.get("href")[0] == "h"):
            publications = (link.get("href"))
        else:
            publications = (url + link.get("href"))

print(publications)

requete.close()