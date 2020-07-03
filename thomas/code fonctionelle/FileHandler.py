from os import path
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import re

list_word_theme =  ["environnement",
                    "chasse",
                    "animaux",
                    "animal",
                    "acca",
                    "oncfs",
                    "louveterie",
                    "gibier",
                    "faune"]


class FileHandler:
    def insert_file(location, pdf):
        """
        methode qui permet de créer un fichier pdf dans le chemin fournir
        -------------------------------------------------------
        location = chemin ou il faut insere le fichier pdf
        pdf = le fichier pdf
        -------------------------------------------------------
        retourne un boleen si l'insertion a marcher true sinon false
        """
        try:
            open(location, 'wb+').write(pdf)
            return True
        except:
            print("il y a un souci lors de l'enregistrement ")

            return False

    def is_exist_file(location):
        """
        methode qui permet de verifier l'existance d'un fichier dans path fournie
        -------------------------------------------------------
        location = chemin vers le fichier
        -------------------------------------------------------
        retourne un boleen true si le fichier existe sinon false
        """
        if path.exists(location):
            return True
        else:
            return False

    def get_content_pdf(path):
        """
        methode qui permet de recuperer le contenu d'un raa en pdf
        -------------------------------------------------------
        path = le chemin vers le pdf
        -------------------------------------------------------
        retourne un dictionaire avec l'in de l'arrete en clef et le contenu de
        l'arreter en valeur
        """
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
        for page in doc:
            page = page.replace('\n\n', '\n')
            list_ligne = page.split("\n")
            titre = ''
            for c, ligne in enumerate(list_ligne):
                if not ligne.isdecimal():
                    titre += ligne
                else:
                    key = re.findall(r'\d{2}-\d{4}-\d{2}-\d{2}-\d{3}', titre)
                    if len(key) == 1:
                        dico[key[0]] = page
                    elif len(key) >= 1 and len(key) <= 2 and key[1] == key[0]:
                        dico[key[0]] = page
                    break
        return dico

    def is_in_theme(page, list_word_theme=list_word_theme):
        match = []
        for word in list_word_theme:
            if word in page.lower():
                match.append(word)
        return match

    def get_all_pdf(path, extension='.pdf'):
        """
        methode qui permet de recuperer tout les fichier avec une
        extention particuliere
        -------------------------------------------------------
        path = la variable du chemin ou l'on veut cherhcer les pdf
        extention = la variable qui selection l'extension rechercher par
        default PDF
        -------------------------------------------------------
        return une liste de path vers des pdf a partir de la racine
        """
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if extension in file:
                    files.append(os.path.join(r, file))
        return(files)
