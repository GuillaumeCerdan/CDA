import requests
from bs4 import BeautifulSoup
import time
import urllib3


# User Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

listurl = ["https://www.chamonix.com/webcam-bochard,48-5051850,fr.html", "https://www.chamonix.com/webcam-parking-grands-montets,48-5052420,fr.html", "https://www.chamonix.com/webcam-telepherique-grands-montets,48-5051853,fr.html"]

for url in listurl:

    print("Le site scrappé : " + url)

    try:
        requete = requests.get(url, headers = header)
        page = requete.content
    except:
        print("erreur de connection 1")
        continue

    soup = BeautifulSoup(page, "html.parser")
    webcam = soup.find_all("img")

    for w in webcam:
        if ("/webcam/" in w['src']): 
            print(w)
            open("webcams/" + w['alt'] + ".jpg", 'wb').write(requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content)

    time.sleep(10)