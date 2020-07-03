import requests
import datetime
import time
from BasicConfig import BasicConfig
from LoggerHandler import LogHandler


class ConnectionHandler:

    def get_page_content(url=BasicConfig.url, header=BasicConfig.header, temporisation=1):
        """
        methode qui permet de se connecter à une page internet grâce à
        une requete http et de renvoyer la page HTML
        -------------------------------------------------------
        url = l'url vers la page
        header = le header de la connection
        temporisation = le temps d'attente entre deux requete
        -------------------------------------------------------
        retourne la page HTML
        """
        time.sleep(temporisation)
        requete = requests.get(url, headers=header)
        page = requete.content
        if not requete.status_code == 200:
            LogHandler.logger_warning(f"erreur de connection vers le lien {url} il y a une erreur {requete.status_code}")
        requete.close()
        return page

    def get_name_PDF(strurl):
        """
        methode qui permet de recupere le nom du
        pdf dans l'url vers le pdf
        -------------------------------------------------------
        strurl = l'url vers le pdf
        -------------------------------------------------------
        retourne le nom du RAA
        """
        new_link_name = strurl.replace('>', '')
        new_link_name = new_link_name.split('/')
        file_name = new_link_name[-1]
        return file_name

    def get_date():
        """
        methode qui permet de generer le mois et l'années courante
        -------------------------------------------------------
        -------------------------------------------------------
        retourne un tuple avec le mois est l'année actuelle
        """
        list_mois = [
                    'Janvier',
                    'Février',
                    'Mars',
                    'Avril',
                    'Mai',
                    'Juin',
                    'Juillet',
                    'Août',
                    'Septembre',
                    'Octobre',
                    'Novembre',
                    'Décembre',
                    ]

        date_now = datetime.datetime.now()
        month = list_mois[date_now.date().month - 1]

        year = date_now.date().year
        return (month, year)
