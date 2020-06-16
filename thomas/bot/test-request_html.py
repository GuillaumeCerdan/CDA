import requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time

url = "http://www.var.gouv.fr/raa"
session = HTMLSession()
header = {'User-Agent': 'Mozilla/5.0'}

try:
    resultat = session.get(url, headers = header)
    print(resultat.status_code)
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("erreur de connection")

resultat.html.render()
for ligne in resultat.html:
    print(ligne)