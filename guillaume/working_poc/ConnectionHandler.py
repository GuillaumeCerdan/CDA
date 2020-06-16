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

    def fetchRessourcesLinks(url = bc.url, retry_strategy = bc.retry_strategy):

        adapter = HTTPAdapter(max_retries=retry_strategy)
        
        http = requests.Session()

        print("url {}".format(url))

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

        links = soup.find_all("a", class_="LienTelecharg")
        list_new_links = [link for link in links]

        print("links {}".format(links))


        # Réupère ceux déjà vérifiés
        link_passed_read = open('links_passed.txt', "r")
        links_already_checked = link_passed_read.readlines()
        link_passed_read.close()

        # Enlève les \n
        for line in links_already_checked:
            line.replace("\n", "")
        
        # Ouvre les deux fichiers en mode append
        link_passed = open('links_passed.txt', "a")
        link_to_add = open('links_to_add.txt', "a")

        urls_raa = []

        for link in list_new_links:

            isIn = False

            for link_already_checked in links_already_checked:

                print("link.attrs('href') {}".format(link.attrs['href']))
                print("link_already_checked {}".format(link_already_checked))

                if link.attrs['href'] in link_already_checked:
                    isIn = True
                    break

            if (not(isIn)):
                urls_raa.append('http://www.ardeche.gouv.fr/' + link.attrs["href"])

        for one_url in urls_raa:
            link_passed.write("{}\n".format(one_url))
            link_to_add.write("{}\n".format(one_url))

        requete.close()
        link_passed.close()
        link_to_add.close()

        print("Il y a eu {} nouveaux RAA".format(len(urls_raa)))

        return urls_raa