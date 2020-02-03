import PyPDF2
import os

for file in os.listdir("pdf_ardeche_septembre"):
    if file.endswith(".pdf"):
        pdfFileObj = open('pdf_ardeche_septembre/' + file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        numPages = pageObj = pdfReader.numPages

        for x in range(numPages):
            print("_" * 10)
            print("Page n° {}".format(str(x)))
            print(pdfReader.getPage(x).extractText())