import requests
from bs4 import BeautifulSoup
import time
import os.path
import logging
from os import path
from datetime import date
from tqdm import tqdm

i = 0
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
test = "pas d'url trouver"
url = "http://www.ardeche.gouv.fr/"
testurl = url
try:
    requete = requests.get(url, headers = header)
    page = requete.content
    print("Première connection passée")
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection")
    print(requete.status_codes)

# Parser html
soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)

list_links = [link.string for link in links]
for link in links:
    
    if  ("recueil" in link.text.lower() ) or ("raa" in link.text.lower()):
        if ("http" in link.attrs['href']):
            url = link.attrs['href']
            break

requete.close()
time.sleep(1)
#--------------------------------------------------------------------------#

try:
    requete = requests.get(url, headers = header, allow_redirects=True)
    page = requete.content
    print("Deuxième connection passée")
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection")
    print(requests.status_codes)

soup = BeautifulSoup(page, "html.parser")
tab = (soup.prettify()).split('"')
URL = [ element for element in tab if ('.html' in element)]
# print(URL)
links = soup.find_all("a", href = True)

#--------------------------------------------------------------------------#

testurl+=URL[0]
print(testurl)
time.sleep(1)

try:
    requete = requests.get(testurl, headers = header, allow_redirects=True)
    page = requete.content
    print("Troisième connection passée")
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection")
    print(requests.status_codes)


soup = BeautifulSoup(page, "html.parser")
links = soup.find_all("a", href = True)
print("connecter a la liste des liste des RAA")

list_links = [link.string for link in links]
listmois = ["janvier 2019","février 2019","mars 2019", "avril 2019","mai 2019","juin 2019","juillet 2019","août 2019","septembre 2019","octobre 2019", "novembre 2019", "décembre 2019"]

for link in tqdm(links):
    for mois in listmois :  
        if  (mois in link.text.lower()):
            test = link.attrs['href']
            
            # print(url+test)
            URLversPdf = url+test

            try:
                requete = requests.get(URLversPdf, headers = header, allow_redirects=True)
                page = requete.content
                print("Requête passée à l'url : {}".format(URLversPdf))
            except:
                # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
                print("Erreur de connection")
                print(requests.status_codes)

                
            soup = BeautifulSoup(page, "html.parser")
            
            links = soup.find_all("a", href = True)
            list_links = [link.string for link in links]
            for link in tqdm(links):
                # Trouve tous les liens pour les recueils
                if (".pdf" in link.get("href")):
                    text_link = link.text
                    requete.close()
                    time.sleep(1)
                    pdf_url = 'http://www.ardeche.gouv.fr/' + link.get("href")
                    requete = requests.get(pdf_url, headers = header)
                    page = requete.content
                    if (not(path.exists("/etc/scriptsPy/pdf_ardeche/" + text_link  + ".pdf"))):
                        open("/etc/scriptsPy/pdf_ardeche/" + text_link.replace('>','')  + ".pdf", 'wb').write(page)
                        i+=1
                        print("Il s'est passé un truc : i = {}".format(i))
                        
today = date.today()
print("Il y a eu "+ str(i) + " pdf déployés le " + str(today) + " sur le département de l'Ardèche")