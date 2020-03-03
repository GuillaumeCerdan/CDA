import requests
import time
import config

class Connecteur:

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"

    requete = None
    page = None

    def __init__(self):
        pass
        

    def get_html(self, url):
        header = {'User-Agent': self.user_agent}
        try:
            self.requete = requests.get(url, headers = header)
            self.page = self.requete.content
        except:
            print("Erreur lors de la connection : erreur {} - à l'url : {}".format(self.requete.status_code, url))

            # Lever une erreur pour plus tard verifier l'url de la prefecture / Analyser le status_code
            # raise Error
        
        # A déplacer plus tard
        time.sleep(1)

        return self.page

    def destroy(self):
        self.requete.close()
        self.requete = None