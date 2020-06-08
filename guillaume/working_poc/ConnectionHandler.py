import requests
import time
from bs4 import BeautifulSoup
import urllib3

from requests.adapters import HTTPAdapter

from decorators import catchableConnection
from BasicConfig import BasicConfig

bc = BasicConfig(7)

print(bc.retry_strategy)

class ConnectionHandler:

    def __init__(self):
        pass

    def fetchRessource(retry_strategy = bc.retry_strategy, url = bc.url):

        adapter = HTTPAdapter(max_retries=retry_strategy)
        
        http = requests.Session()

        http.mount("https://", adapter)
        http.mount("http://", adapter)

        http.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
        })


        time.sleep(1)
        requete = http.get(url)
        reponse = requete.content

        requete.close()
        return reponse

    def fetchRessourcesLinks(retry_strategy = bc.retry_strategy, url = bc.url):

        adapter = HTTPAdapter(max_retries=retry_strategy)
        
        http = requests.Session()

        http.mount("https://", adapter)
        http.mount("http://", adapter)

        http.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
        })

        time.sleep(1)

        requete = http.get(url)
        reponse = requete.content

        requete.close()

        soup = BeautifulSoup(reponse, "html.parser")

        links = soup.find_all("a", href = True)
        liste_lien = [link for link in links if "raa" in link.attrs['href'] and "pdf" in link.attrs['href'] ]

        link_passed = open('links_passed.txt', "w+")
        link_to_add = open('links_to_add.txt', "w+")

        lines_in_file = link_passed.readlines() 

        urls_raa = []

        nouveaux_raa = 0

        for lien in liste_lien:

            isIn = False

            for line in lines_in_file:

                if line == lien:
                    isIn = True

            if (not(isIn)):
                nouveaux_raa + 1
                urls_raa.append('http://www.ardeche.gouv.fr/' + lien.attrs["href"])

        for one_url in urls_raa:
            link_passed.write("{}\n".format(one_url))
            link_to_add.write("{}\n".format(one_url))

        requete.close()

        print("Il y a eu {} nouveaux RAA".format(nouveaux_raa))

        return urls_raa

# Prendre en compte le status_code