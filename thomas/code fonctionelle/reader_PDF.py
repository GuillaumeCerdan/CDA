from FileHandler import FileHandler
import json
import requests


path = "pdf-ardeche/"
url_post = "http://127.0.0.1:5000/add_arrete"
all_url_pdf = FileHandler.get_all_pdf(path)
for url_pdf in all_url_pdf:
    raa = FileHandler.get_content_pdf(url_pdf)
    for arrete in raa:
        if FileHandler.is_in_theme(raa[arrete]):
            with open('arreteValide.json', 'a+', encoding='UTF-8') as file:
                file.write(json.dumps({arrete: raa[arrete]}))
                requests.post(url_post, data={"id_arrete": arrete,
                                              "extrait": raa[arrete]})
