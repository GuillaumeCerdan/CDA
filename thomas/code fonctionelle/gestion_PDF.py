import FileHandler
import json

dico  =  FileHandler.get_content_pdf()

with open('file.txt', 'w', encoding='UTF-8') as file:
     file.write(json.dumps(dico))

print('fini')