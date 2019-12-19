import globals
import getPageRaa

print("Récupération des recueils")
print("")
# print (links)

i = 0

list_links = [link.string for link in getPageRaa.links]
# listmois = ["janvier 2019","février 2019","mars 2019", "avril 2019","mai 2019","juin 2019","juillet 2019","août 2019","septembre 2019","octobre 2019", "novembre 2019", "décembre 2019"]
listmois = ["décembre 2019"]

for link in getPageRaa.links:
    # print (link.text  + " = " + link.attrs["href"])
    # print(link.attrs['href'])
    for mois in listmois :  
        if  (mois in link.text.lower()):
            test = link.attrs['href']
            
            # print(url+test)
            URLversPdf = globals.url+test

            try:
                requete = globals.requests.get(URLversPdf, headers = globals.header, allow_redirects=True)
                page = requete.content
            except:
                # faire relever une erreur afin ce verifier l'url de la prefecture ou autre
                print("erreur de connection")
                print(requete.status_codes)

                
            soup = globals.BeautifulSoup(page, "html.parser")
            
            links = soup.find_all("a", href = True)
            list_links = [link.string for link in links]
            for link in globals.tqdm(links):
                # Trouve tous les liens pour les recueils
                if (".pdf" in link.get("href")):
                    text_link = link.text
                    requete.close()
                    globals.time.sleep(1)
                    pdf_url = 'http://www.ardeche.gouv.fr/' + link.get("href")
                    requete = globals.requests.get(pdf_url, headers = globals.header)
                    page = requete.content
                    # print( str(not(path.exists("pdf_ardeche/" +text_link  + ".pdf"))) +" "+ text_link  + ".pdf")
                    if (not(globals.path.exists("pdf_ardeche/" + text_link  + ".pdf"))):
                        open("pdf_ardeche/" + text_link.replace('>','')  + ".pdf", 'wb').write(page)
                        i+=1
today = globals.date.today()
print("")
print('Il y a eu ' + str(i) + ' pdf deployé le ' + str(today) + " sur le département de l'Ardèche")