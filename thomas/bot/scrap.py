import requests
from bs4 import BeautifulSoup
import time

# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

listurl = ["http://www.var.gouv.fr", "http://www.vaucluse.gouv.fr", "http://www.alpes-maritimes.gouv.fr", "http://www.alpes-de-haute-provence.gouv.fr", "http://www.hautes-alpes.gouv.fr", "http://www.bouches-du-rhone.gouv.fr"]
test_Url = []

for url in listurl:
    time.sleep(1)
    goodurl =  url

    print("Le site scrappé : " + goodurl)

    #Url à parcourir
    # try catch pour verifier si la connection fonctione sinon on passe cette url
    try:
        requete = requests.get(goodurl, headers = header)
        page = requete.content
    except:
        # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
        print("erreur de connection")
        continue


    # Parser html
    soup = BeautifulSoup(page, "html.parser")

    # Tous les liens
    links = soup.find_all("a", href = True)
    titles = soup.find_all("h1")
    spans = soup.find_all("span")

    #mise en place des tableaux avec les liens
    list_links = [link.string for link in links]
    list_titles = [title.string for title in titles]
    list_spans = [span.string for span in spans]

    for link in links:
        # print (link.text  + " = " + link.attrs["href"])
        # print(link.attrs['href'])
        
        if  ("recueil" in link.text.lower() ) or ("raa" in link.text.lower()):
            if ("http" in link.attrs['href']):
                test_Url.append(link.attrs["href"])
            if ("/"not in link.attrs['href']):
                test_Url.append(goodurl + "/"+link.attrs['href'])
            else:
                test_Url.append(goodurl + link.attrs['href'])
            break
print(test_Url)
