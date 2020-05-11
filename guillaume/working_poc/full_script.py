from bs4 import BeautifulSoup
import datetime

from PdfHandler import PdfHandler
from ConnectionHandler import ConnectionHandler

# Date Handler
list_mois = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

date_now = datetime.datetime.now()

#month = list_mois[date_now.date().month - 1]
month = "Mars"
year = date_now.date().year


page = ConnectionHandler.getPageContent()
soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)
print("Connecté à la liste des liste des RAA du mois de {}".format(month))


list_links = [link.attrs['href'] for link in links if link.string == "{} {}".format(month,year)]
url = list_links[0]

page = ConnectionHandler.getPageContent('http://www.ardeche.gouv.fr/' + url)

soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)
liste_lien = [link for link in links if "raa" in link.attrs['href'] and "pdf" in link.attrs['href'] ]

nb_new_pdfs = 0
new_pdfs = []

for lien in liste_lien:

    pdf_url = 'http://www.ardeche.gouv.fr/' + lien.attrs["href"]

    page = ConnectionHandler.getPageContent(pdf_url)

    new_link_name = lien.text.replace('>','')
    
    if (not(PdfHandler.doesPdfExistsAt("pdf-ardeche/" + new_link_name  + ".pdf"))):
        PdfHandler.insertPdfAt("pdf-ardeche/" + new_link_name  + ".pdf", page)
        print("C'est un nouveau RAA")
        nb_new_pdfs += 1
        new_pdfs.append(new_link_name)


if (nb_new_pdfs > 0):
    if (nb_new_pdfs == 1):
        print("Il y a eu 1 PDF rajouté")
        print("Le voici : {}".format(new_pdfs))
    else:
        print("Il y a eu {} PDFs rajoutés".format(nb_new_pdfs))
        print("Les voici : {}".format(new_pdfs))