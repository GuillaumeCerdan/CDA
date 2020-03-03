import time
import os.path
import logging
from bs4 import BeautifulSoup
from os import path
from datetime import date
from connecteur import Connecteur
import config



connecteur = Connecteur()
page = connecteur.get_html("http://www.ardeche.gouv.fr/")


# Html parser
soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)

list_links = [link.string for link in links]
urls = []

for link in links:
    
    # A remplacer par un sélecteur XPATH
    if  ("recueil" in link.text.lower() ) or ("raa" in link.text.lower()):
        if ("http" in link.attrs['href']):
            urls.append(link.attrs['href'])
            break


# Fermeture de la connection
connecteur.destroy()

# Timeout
time.sleep(config.average_timeout)

print("urls : {}".format(urls))


