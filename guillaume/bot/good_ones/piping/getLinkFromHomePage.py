import globals

test = "Pas d'url trouvé"
testurl = globals.url
print("Connection en cours au site de l'ardèche")

# Progress Bar
# for j in tqdm(range(0, 4)):
#     time.sleep(randint(1, 50) / 100)

# print("")

try:
    requete = globals.requests.get(globals.url, headers = globals.header)
    page = requete.content
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection au site : " + globals.url)
    print(requete.status_codes)


soup = globals.BeautifulSoup(page, "html.parser")
links = soup.find_all("a", href = True)
list_links = [link.string for link in links]

for link in links:    
    if  ("recueil" in link.text.lower() ) or ("raa" in link.text.lower()):
        if ("http" in link.attrs['href']):
            url_raa_page = link.attrs['href']
            break
requete.close()
globals.time.sleep(1)
print ("Url récupéré de la page d'accueil : " + url_raa_page)

# print("Traitement du JavaScript")
# for j in tqdm(range(0, 20)):
#     time.sleep(randint(1, 30) / 100)

# print("")

#--------------------------------------------------------------------------#
