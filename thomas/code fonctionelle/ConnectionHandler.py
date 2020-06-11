import requests
import time

from decorators import catchableConnection
from BasicConfig import BasicConfig

class ConnectionHandler:

    def __init__(self):
        print('ConnectionHandler inited')

    def getPageContent(url = BasicConfig.url, header = BasicConfig.header):
        time.sleep(1)
        requete = requests.get(url, headers = header)
        page = requete.content

        print("Connection à {} réussie".format(url))

        requete.close()
        return page