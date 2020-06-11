from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
import io
import os
import re
import json




fp = open('echantillonTestPdf/Recueil RAA N07-2019-001 du 03 janvier 2019 - Spécial tous services.pdf', 'rb')
rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
print(type(retstr))
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
doc = []
dico = dict()
for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
    interpreter.process_page(page)
    data = retstr.getvalue()
    doc.append(data)
    data = ''
    retstr.truncate(0)
    retstr.seek(0)
listtitre = []

# print(len(doc))
for page in doc:
    # print('----------')
    # 
    # print(page)
    # print("-----")
    page = page.replace('\n\n', '\n')
    list_ligne = page.split("\n")
    # print ('le titre est')
    titre = ''
    for c, ligne in enumerate(list_ligne):
        if not ligne.isdecimal() :
            # print (ligne)
            titre += ligne 
        else:
            # print (titre)
            # print(re.findall(r'\d\d-\d\d\d\d-\d\d-\d\d-\d\d\d', titre))
            
            key = re.findall(r'\d\d-\d\d\d\d-\d\d-\d\d-\d\d\d', titre)
            # print(key)
            if len(key) ==1:
                dico[key[0]] =  page
            elif len(key)>=1 and len(key)<=2 and key[1] == key[0]:
                dico[key[0]] =  page
            # print(dico)

            break
# print(f'les titres sont \n__________\n{setlisttitre}| {len(listtitre)} | {len(setlisttitre)}\n__________')
print(dico)

with open('file.txt', 'w', encoding='UTF-8') as file:
     file.write(json.dumps(dico))

print('fini')
