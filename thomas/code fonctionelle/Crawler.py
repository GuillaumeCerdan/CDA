
from bs4 import BeautifulSoup
from ConnectionHandler import ConnectionHandler


domaine = 'http://www.ardeche.gouv.fr/'
month, year = ConnectionHandler.get_date()

page = ConnectionHandler.get_page_content()
soup = BeautifulSoup(page, "html.parser")


links = soup.find_all("a", href=True)


list_links = [link.attrs['href'] for link in links if link.string == f"{month} {year}"]
url = list_links[0]

page = ConnectionHandler.get_page_content(domaine + url)

soup = BeautifulSoup(page, "html.parser")
# with est un contexte manager
with open("lienCrawler.txt", mode='r+', encoding='UTF-8' ) as f:
    contenu_txt = f.read()

links = soup.find_all("a", class_="LienTelecharg", href=True)
liste_liens = [domaine + link.attrs['href'] for link in links if "pdf" in link.attrs['href']]
liste_liens_inconnus = {lien for lien in liste_liens if lien not in set(contenu_txt.split('\n'))}

with open("lienCrawler.txt", mode='a+', encoding='UTF-8') as f:
    for lien in liste_liens_inconnus:
        f.write(lien)
        f.write('\n')
