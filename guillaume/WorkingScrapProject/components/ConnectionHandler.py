# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import urllib3

from requests.adapters import HTTPAdapter

from decorators import catchableConnection
from components.CrawlConfig import CrawlConfig

bc = CrawlConfig(7)

class ConnectionHandler:

    def __init__(self):
        pass
    
    
    def fetch_ressource(retry_strategy = bc.retry_strategy, url = bc.url):

        """
            Connexion simple retournant le contenu de la page
            =================================================

            Utilise une stratégie de retry, soit celle donnée soit celle de la config initiale.
            Se connecte à un url donné si précisé, sinon à l'url de la config initiale.

            :param retry_strategy: Retry Object defined by default in CrawlConfig
            :param url: String (url) to connect to defined by default in CrawlConfig
            :type retry_strategy: Retry Object from requests.packages.urllib3.util.retry
            :type url: String
            :return: Crawled page
            :rtype: String
        """

        adapter = HTTPAdapter(max_retries=retry_strategy)
        
        http = requests.Session()

        http.mount("https://", adapter)
        http.mount("http://", adapter)

        http.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
        })

        # Une seconde de timeout pour ne pas flood les préfectures si fonction appelée plusieurs fois
        time.sleep(1)

        requete = http.get(url)
        reponse = requete.content

        requete.close()
        return reponse

    def fetch_ressource_links(url = bc.url, retry_strategy = bc.retry_strategy):

        
        """
            Connexion poussée retournant le nombre de nouveaux RAA en fonction du fichier 
            data-txt/links_to_add.txt
            =================================================

            Utilise une stratégie de retry, soit celle donnée soit celle de la config initiale.
            Se connecte à un url donné si précisé, sinon à l'url de la config initiale.

            :param url: String (url) to connect to defined by default in CrawlConfig
            :param retry_strategy: Retry Object defined by default in CrawlConfig
            :type url: String
            :type retry_strategy: Retry Object from requests.packages.urllib3.util.retry
            :return: List of new RAA
            :rtype: List<String>
        """

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

        links = soup.find_all("a", class_="LienTelecharg")
        list_new_links = [link for link in links]

        # Réupère ceux déjà vérifiés
        link_passed_read = open('data-txt/links_passed.txt', "r")
        links_already_checked = link_passed_read.readlines()
        link_passed_read.close()

        # Enlève les \n
        for line in links_already_checked:
            line.replace("\n", "")
        
        # Ouvre les deux fichiers en mode append
        link_passed = open('data-txt/links_passed.txt', "a")
        link_to_add = open('data-txt/links_to_add.txt', "a")

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