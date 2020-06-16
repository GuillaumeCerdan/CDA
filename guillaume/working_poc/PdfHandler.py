from os import path
from io import StringIO

import PyPDF2

class PdfHandler:

    def __init__(self) :
        print('PdfHandler inited')

    def insertPdfAt(location, pdf) :
        # TODO asserts
        try:
            file = open(location, 'wb').write(pdf)
            file.close()
            return True
        except:
            return False

    def doesPdfExistsAt(location) :
        # TODO asserts
        if path.exists(location) :
            return True
        else:
            return False


    def insertPdfTextAt(pdf_location, desired_location):
        
        # TODO asserts + switch sur Tesseract si c'est des images

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

