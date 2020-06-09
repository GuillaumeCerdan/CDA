# -*- coding: utf-8 -*-

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
import io
import os
import re
import fitz

from components.CrawlConfig import CrawlConfig

bc = CrawlConfig(7)

class PdfHandler:

    def __init__(self) :
        pass

    def insert_pdf_at(self, location, pdf) :

        """
            Insère un fichier à un endroit donné
            =================================================

            Insère un fichier donné à un endroit donné. Retourne True si le fichier est bien déplacé
            et False s'il y a eu une erreur lors du processus.

            :param location: Url de l'endroit où déplacer le fichier
            :param pdf: Lien du fichier à déplacer
            :type location: Sring
            :type pdf: String
            :return: HasBeenSuccessful
            :rtype: Boolean
        """

        try:
            file = open(location, 'wb').write(pdf)
            file.close()
            return True
        except:
            return False

    def does_pdf_exists_at(self, location) :
        
        """
            Retourne si un fichier existe à un endroit donné
            =================================================

            Vérifie si un nom de fichier donné existe ou non.

            :param location: Url du fichier à vérifier
            :type location: Sring
            :return: DoesItExists
            :rtype: Boolean
        """

        if path.exists(location) :
            return True
        else:
            return False

    def insert_pdf_at(self, pdf_location, desired_location):
        
        """
            Insère le contenu d'un fichier pdf à un endroit donné
            =================================================

            Récupère le contenu d'un pdf et l'insère dans un endroit donné (dans un fichier .txt).
            Retourne True si ça s'est bien passé et False s'il y a eu un problème dans le processus.

            :param pdf_location: Url du fichier dont on veut le contenu
            :param desired_location: Url de l'endroit où insérer le contenu de 'pdf_location'
            :type pdf_location: Sring
            :type desired_location: Sring
            :return: DidItWork
            :rtype: Boolean
        """

        try:
            pdfFileObj = open(pdf_location, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            numPages = pdfReader.numPages

            file = open(desired_location, 'w+')

            for x in range(numPages):
                page = pdfReader.getPage(x).extractText()
                file.write(page)

            file.close()

            # For exception handling
            return True

        except:
            return False


    def get_pdf_content(self, pdf_file):

        """
            Retourne le contenu d'un PDF page par page dans une liste.
            ==========================================================

            Récupère le contenu d'un pdf et l'insère page après page dans une liste.
            Retourne le tout.

            :param pdf_file: Url du fichier dont on veut le contenu
            :type pdf_file: String
            :return: List contenant le contenu d'une page chacune
            :rtype: List<String>
        """

        fp = open(pdf_file, 'rb')
        ressources_manager = PDFResourceManager()
        string_io = io.StringIO()
        laparams = LAParams()
        device = TextConverter(ressources_manager, string_io,  laparams=laparams)
        interpreter = PDFPageInterpreter(ressources_manager, device)
        doc = []
        dico = dict()
        for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
            interpreter.process_page(page)
            data = string_io.getvalue()
            doc.append(data)
            data = ''
            string_io.truncate(0)
            string_io.seek(0)
        fp.close()
        return doc

    def get_matching_pages(self, pdf_file, matchers = CrawlConfig.matchers):
        """
            Retourne les pages d'un PDF qui matchent avec un 
            ou plusieurs mots clés.
            ==========================================================

            Récupère le contenu d'un pdf et regarde si le contenu page par page 
            matche avec le(s) mot-clé(s)

            :param pdf_file: Url du fichier dont on veut le contenu qui matche
            :param matchers: Liste de mots clés à vérifier si ils matchent
            :type pdf_file: String
            :type matchers: List<String>
            :return: List contenant le contenu de chaque page qui matche
            :rtype: List<String>
        """
        content = self.get_pdf_content(pdf_file)
        matchings = []
        for page in content:
            for matcher in matchers:
                if matcher in page:
                    matchings.append(page)
        return matchings



    def get_matching_pages_from_pdfs(self, pdf_files, matchers = CrawlConfig.matchers):

        # En cours de développement

        """
            Retourne les pages d'une liste de PDF qui matchent avec un 
            ou plusieurs mots clés.
            ==========================================================

            Récupère le contenu des pdf et regarde si le contenu 
            page par page matche avec le(s) mot-clé(s). Si oui, 
            il retourne une liste de dictionnaires contenant :
            {'mot clé' : {'fichier en question': 'index de page qui matche'}}

            :param pdf_files: Liste d'url de fichiers dont on veut le contenu qui matche
            :param matchers: Liste de mots clés à vérifier si ils matchent
            :type pdf_file: String
            :type matchers: List<String>
            :return: List contenant un dictionnaire par mot clé matché et les pages du pdf concerné
            :rtype: List<Dictionary{Dictionary{}}>

        """

        matchings = []
        for pdf_file in pdf_files:
            content = self.get_pdf_content(pdf_file)
            for page in content:
                for matcher in matchers:
                    if matcher in page:
                        matchings.append(
                            {matcher: {
                                pdf_file: page.index
                            }}
                        )
        return matchings


    def pdf_to_img(self, pdf_file, index):

        """
            Convertit une page donnée d'un pdf en Image PNG
            =================================================

            Reçoit un pdf et le transforme en plusieurs Images PNG (une pour chaque page dans le PDF)

            :param pdf_file: Url du pdf à transformer
            :param index: Numéro de la page à transformer
            :type pdf_file: String
            :type index: Int
            :return: Lien vers l'image
            :rtype: String
        """

        return pdf2jpg.convert_pdf2jpg(pdf_file, "pdf-ardeche-img/", dpi=300, pages=str(index))

    def ocr_core(self, file):

        """
            Retourne le texte en format String de l'image donnée
            =================================================

            Reçoit un lien vers une Image et détecte le contenu via Tesseract.
            Retourne le contenu directement.

            :param file: Url de l'image dont le contenu est à détecter
            :type file: String
            :return: Le contenu texte de l'image
            :rtype: String
        """

        text = pytesseract.image_to_string(file)
        return text

    def print_page_at_index(self, pdf_file, index):

        """
            Retourne le texte en format String de la page (scannée) d'un PDF donné
            =================================================

            Reçoit un lien vers un PDF et un numéro de page puis convertit cette page en Image
            et détecte le contenu via Tesseract. Retourne le contenu directement.

            :param pdf_file: Url de l'image dont le contenu est à détecter
            :param index: Numéro de la page dont on veut le contenu
            :type pdf_file: String
            :type index: Int
            :return: Le contenu texte de l'image
            :rtype: String
        """

        images = pdf_to_img(pdf_file, index)
        print(images[0])
        return ocr_core(images)

    def is_it_full_text(self, pdf_location):
        if ()
