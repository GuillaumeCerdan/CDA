from os import path
from io import StringIO

import PyPDF2

class PdfHandler:

    def __init__(self) :
        pass

    def insert_pdf_at(location, pdf) :

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

    def does_pdf_exists_at(location) :
        
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

    def insert_pdf_at(pdf_location, desired_location):
        
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

    def getContentFromPdf(pdf_file, index):

        try:
            pdfFileObj = open(pdf_file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            # numPages = pdfReader.numPages

            content = pdfReader.getPage(index).extractText()

            print(content)

            pdfFileObj.close()

            return True

        except:
            return False

    def pdf_to_img(pdf_file, index):

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

    def ocr_core(file):

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

    def print_page_at_index(pdf_file, index):

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