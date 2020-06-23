import requests
import time

from decorators import catchableConnection
from BasicConfig import BasicConfig
from LoggerHandler import LogHandler

class ConnectionHandler:

    def __init__(self):
        print('ConnectionHandler inited')

    def getPageContent(url = BasicConfig.url, header = BasicConfig.header, temporisation = 1):
        time.sleep(temporisation)
        requete = requests.get(url, headers = header)
        page = requete.content
        if not requete.status_code == 200:
            LogHandler.logger_warning(f"erreur de connection vers le lien {url}")
            # logger
            

        requete.close()
        return page
    
    def get_name_PDF(strurl):
        new_link_name = strurl.replace('>','')
        new_link_name = new_link_name.split('/')
        file_name  = new_link_name[-1]
        return file_name