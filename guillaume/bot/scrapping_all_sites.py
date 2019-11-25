import os
import csv
import requests
import sys
import fileinput
from bs4 import BeautifulSoup
import time


# User Agent
header = {'User-Agent': 'Mozilla/5.0'}

url = "http://www.prefectures-regions.gouv.fr/"


try:
    requete = requests.get(url, headers = header)
    page = requete.content
except:
    print("erreur de connection 1")


soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href = True)
already_passed = False
for link in links:
    if ("provence-alpes-cote-dazur" in link.get("href").lower() and not already_passed):
        print("Navigating to : http://www.prefectures-regions.gouv.fr" + link.get("href"))
        try:
            requete.close()
            requete = requests.get("http://www.prefectures-regions.gouv.fr" + link.get("href"), headers = header)
            page = requete.content
            soup = BeautifulSoup(page, "html.parser")
            already_passed = True
            #pass = True
        except:
            print("erreur de connection 2")
            
            #pass = False

        #if (pass):
        other_links = soup.find_all("a", href = True)
        for other_link in other_links:
            if ("raa" in other_link.get("href").lower() and "2019" in other_link.get("href") and not "draa" in other_link.get("href").lower()):
                print("Lien vers les RAA de Provence Alpes Côte D'Azur : " + other_link.get("href"))
                try:
                    requete.close()
                    requete = requests.get("http://www.prefectures-regions.gouv.fr" + other_link.get("href"), headers = header)
                    page = requete.content
                    soup = BeautifulSoup(page, "html.parser")
                    #pass = True
                except:
                    print("erreur de connection 2")
                    #pass = False
                
                last_links = soup.find_all("a", href = True)
                for last_link in last_links:
                    if ("pdf" in last_link.get("href").lower()):
                        print("Lien vers un pdf : " + last_link.get("href"))


        