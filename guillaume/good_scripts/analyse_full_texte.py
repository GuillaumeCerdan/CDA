import PyPDF2
import os

iterator = 0
nb_global = 0
suivi = {}
for file in os.listdir("pdf_ardeche12"):

    pdfFileObj = open('pdf_ardeche12/' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages

    iterator += numPages
    nb_environnement = 0
    for x in range(numPages):
        page = pdfReader.getPage(x).extractText()
        if ("installations classées" in page):
            nb_environnement += 1
            suivi[x] = nb_environnement
    if (not (suivi == {})):
        print(file)
        print(suivi)
    suivi = {}