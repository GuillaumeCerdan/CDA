import PyPDF2

pdfFileObj = open("good-pdfs/recueil-07-2020-052-recueil-des-actes-administratifs-special_1_.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# numPages = pdfReader.numPages
content = pdfReader.getPage(3).extractText()

print(content)

pdfFileObj.close()
