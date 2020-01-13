import globals
import getLinkFromHomePage

try:
    requete = globals.requests.get(getLinkFromHomePage.url_raa_page, headers = globals.header, allow_redirects=True)
    page2 = requete.content
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("erreur de connection")
    print(globals.requests.status_codes)

soup = globals.BeautifulSoup(page2, "html.parser")
# print((soup.prettify()).split('"'))
tab = (soup.prettify()).split('"')
URL = [ element for element in tab if ('.html' in element)]
# print(URL)
links = soup.find_all("a", href = True)

#--------------------------------------------------------------------------#



getLinkFromHomePage.testurl+=URL[0]
print("Url des liens des recueils : " + getLinkFromHomePage.testurl)
globals.time.sleep(1)

try:
    requete = globals.requests.get(getLinkFromHomePage.testurl, headers = globals.header, allow_redirects=True)
    page = requete.content
except:
    # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
    print("Erreur de connection à l'url : " + getLinkFromHomePage.testurl)
    print(globals.requests.status_codes)


soup = globals.BeautifulSoup(page, "html.parser")
#print(soup.prettify())
links = soup.find_all("a", href = True)

# for j in tqdm(range(0, 6)):
#     time.sleep(randint(1, 70) / 100)

# print("")

print("Connecté à la liste des liste des RAA")
print("")
