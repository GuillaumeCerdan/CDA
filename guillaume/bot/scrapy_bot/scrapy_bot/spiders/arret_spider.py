import scrapy
from time import sleep


class ArretSpider(scrapy.Spider):
    name = "arret"

    def start_requests(self):
        urls = [
            'http://www.ardeche.gouv.fr/recueil-des-actes-administratifs-r791.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.css('#main a'):
            sleep(1)
            if ('.pdf' in a):
                print("YEN A UN : {}".format(a))
                yield response.follow(a, callback=self.parse)