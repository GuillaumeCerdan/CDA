import PyPDF2
import os

iterator = 0
nb_global = 0
suivi = {}

config = ["dérogation", "espèces", "protégées"]

for file in os.listdir("bouches_du_rhone_2019"):

    pdfFileObj = open('bouches_du_rhone_2019/' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages

    iterator += numPages
    nb_environnement = 0
    for x in range(numPages):
        page = pdfReader.getPage(x).extractText()

        for item in config:

            if (item in page):
                nb_environnement += 1
                suivi[x] = "{} : {}".format(nb_environnement, item)

    if (not (suivi == {})):
        print(file)
        print(suivi)
    suivi = {}

