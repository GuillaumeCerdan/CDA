import requests
from bs4 import BeautifulSoup
import time

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

url = "http://www.ardeche.gouv.fr/"

try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("erreur de connection")
    print(requete.status_codes)

# Parser html
soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a", href = True)

list_links = [link.string for link in links]
for link in links:
    # print (link.text  + " = " + link.attrs["href"])
    # print(link.attrs['href'])
    
    if  ("recueil" in link.text.lower() ) or ("raa" in link.text.lower()):
        if ("http" in link.attrs['href']):
            url = link.attrs['href']
            break
requete.close()
time.sleep(3)
print (url)
#--------------------------------------------------------------------------#

try:
    requete = requests.get(url, headers = header, allow_redirects=True)
    page = requete.content
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("erreur de connection")
    print(requests.status_codes)

soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

links = soup.find_all("a", href = True)

list_links = [link.string for link in links]
for link in links:
    # print (link.text  + " = " + link.attrs["href"])
    # print(link.attrs['href'])
    
    if  ("janvier" in link.text.lower()):
        url = link.attrs['href']
        break
print(url)