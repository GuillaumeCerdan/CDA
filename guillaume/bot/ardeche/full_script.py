import requests
from bs4 import BeautifulSoup
import time
import datetime
from os import path
import os

list_mois=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
 
dat = datetime.datetime.now()
mois = dat.date().month
current_month = list_mois[mois-1]
year = dat.date().year

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

# url direct vers la liste des mois pour la recuperation des RAA 
url = "http://www.ardeche.gouv.fr/recueil-des-actes-administratifs-r791.html"


try:
    requete = requests.get(url, headers = header)
    page = requete.content
    print("Première connection passée")
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection")
    print(requete.status_codes)


soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)
print("connecter a la liste des liste des RAA")


list_links = [link.attrs['href'] for link in links if link.string == "{} {}".format(current_month,year)]
print(list_links)
url = list_links[0]
print(url)


try:
    requete = requests.get('http://www.ardeche.gouv.fr/' + url, headers = header)
    page = requete.content
    print("deuxieme connection passée")
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection")
    print(requete.status_codes)
soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)
liste_lien = [link for link in links if "raa" in link.attrs['href'] and "pdf" in link.attrs['href'] ]

for lien in liste_lien:
    print(lien)
    pdf_url = 'http://www.ardeche.gouv.fr/' + lien.attrs["href"]
    print(pdf_url)
    requete = requests.get(pdf_url, headers = header)
    page = requete.content

    new_link_name = lien.text.replace('>','')
    
    if (not(path.exists("pdf-ardeche/" + new_link_name  + ".pdf"))):
        open("pdf-ardeche/" + new_link_name  + ".pdf", 'wb').write(page)

    if (not(path.exists("pdf-ardeche-text/" + lien.text  + ".pdf"))):
        insertTextFromPdfAt(location, pdf)

    time.sleep(1)


def insertTextFromPdfAt(location, pdf):
    open("pdf-ardeche/" + lien.text.replace('>','')  + ".pdf", 'wb').write(page)