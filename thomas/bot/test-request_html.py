import requests_html
from bs4 import BeautifulSoup
import time

url = "http://www.var.gouv.fr"

try:
    requete = requests.get(goodurl, headers = header)
    page = requete.content
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("erreur de connection")


