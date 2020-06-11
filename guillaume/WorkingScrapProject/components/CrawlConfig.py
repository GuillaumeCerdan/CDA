# -*- coding: utf-8 -*-

from requests.packages.urllib3.util.retry import Retry

class CrawlConfig:

    # Scrapper Config Handler
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    url = "http://www.ardeche.gouv.fr/recueil-des-actes-administratifs-r791.html"
    base_url = "http://www.ardeche.gouv.fr/"

    matchers = ["a", "pollution", "particule fine", "changement climatique", "OGM", "déchets", "empreinte écologique", "a"]


    def __init__(self, max_retries) :
        self.retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )