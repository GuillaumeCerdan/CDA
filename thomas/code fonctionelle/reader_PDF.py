from PdfHandler import PdfHandler
import get_file
import json


all_url_pdf = get_file.getAllfile("pdf-ardeche/")
for url_pdf in all_url_pdf:
    raa = PdfHandler.get_content_pdf(url_pdf)
    for arrete in raa:
        if PdfHandler.is_in_theme(raa[arrete]):
            with open('arreteValide.json', 'a+', encoding='UTF-8') as file:
                file.write(json.dumps({arrete: raa[arrete]}))