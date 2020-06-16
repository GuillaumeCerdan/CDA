
from bs4 import BeautifulSoup
import os
import datetime

from PdfHandler import PdfHandler
from ConnectionHandler import ConnectionHandler

# Date Handler
list_mois = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

date_now = datetime.datetime.now()
month = list_mois[date_now.date().month - 1]

year = date_now.date().year


page = ConnectionHandler.getPageContent()
soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)
print("Connecté à la liste des liste des RAA du mois de {}".format(month))


list_links = [link.attrs['href'] for link in links if link.string == "{} {}".format(month,year)]
url = list_links[0]

page = ConnectionHandler.getPageContent('http://www.ardeche.gouv.fr/' + url)

soup = BeautifulSoup(page, "html.parser")

f = open("lienCrawler.txt", mode='r+' )
contenuTxt = f.read()
f.close()
links = soup.find_all("a",class_="LienTelecharg", href = True)
liste_liens = ['http://www.ardeche.gouv.fr/' + link.attrs['href'] for link in links if "pdf" in link.attrs['href'] ]
liste_lien_inconue = {lien for lien in liste_liens if lien not in set(contenuTxt.split('\n'))}

f = open("lienCrawler.txt", mode='a+')
for lien in liste_lien_inconue:
    f.write(lien)
    f.write('\n')
f.close()