import scrapy
from time import sleep


class ArretSpider(scrapy.Spider):
    name = "arret"

    def start_requests(self):
        urls = [
            'http://www.ardeche.gouv.fr/janvier-2020-a9511.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.css('a::attr(href)'):
            sleep(1)
            if ('.pdf' in a):
                print("1 PDF TROUVÉ : {}".format(a))
                yield response.follow(a, callback=self.parse)