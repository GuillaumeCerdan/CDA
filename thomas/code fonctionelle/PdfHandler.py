from os import path
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
import io
import re
import json


class PdfHandler:

    def __init__(self) :
        print('PdfHandler inited')

    def insertPdfAt(location, pdf) :
        # TODO asserts

        try:
            open(location, 'wb+').write(pdf)
            return True
        except:
            print("il y a un souci lors de l'enregiqtrement ")

            return False

    def doesPdfExistsAt(location) :
        # TODO asserts
        if path.exists(location) :
            return True
        else:
            return False
    
    def get_content_pdf(path):
        fp = open(path, 'rb')
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        # print(type(retstr))
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
                    elif len(key)>=1 and len   (key)<=2 and key[1] == key[0]:
                        dico[key[0]] =  page
                    # print(dico)

                    break
        return dico
    
    def is_in_theme(page, list_word_theme = ["environement","chasse", "animaux",  "animal","acca", "oncfs" , "louveterie","gibier","faune"]  ):
        for word in list_word_theme:
            if word in page.lower():
                print('find one')
                return True
            else:
                print('not found')
        return False

    def getAllPdf (path , extention = '.pdf'):
        '''
        path = la variable du chemin ou l'on veut cherhcer les pdf 
        extention = la variable qui selection 'lextention rechercher par default PDF
        return une liste de path vers des pdf a partir de la racine (C:)
        '''
            
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if extention in file:
                    files.append(os.path.join(r, file))
        return(files)

