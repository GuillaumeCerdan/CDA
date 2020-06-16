# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
from sys import argv
import os
import argparse

from components.ConnectionHandler import ConnectionHandler
from components.CrawlConfig import CrawlConfig


# Date Handler
list_mois = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
date_now = datetime.datetime.now()

# Si argument passé en ligne de commande
if (argv[-1] in list_mois):
    month = argv[-1]
else:
    month = list_mois[date_now.date().month - 2]

year = date_now.date().year

# Se connecte à la page listant les RAA
page = ConnectionHandler.fetch_ressource()
soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)

print("Connecté à la liste des liste des RAA du mois de {}".format(month))

list_links = [link.attrs['href'] for link in links if link.string == "{} {}".format(month,year)]
url = list_links[0]

urls_raa = ConnectionHandler.fetch_ressource_links(CrawlConfig.base_url + url)