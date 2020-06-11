

class BasicConfig:

    # Scrapper Config Handler
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    url = "http://www.ardeche.gouv.fr/recueil-des-actes-administratifs-r791.html"

    def __init__(self) :
        print("BasicConfig inited")