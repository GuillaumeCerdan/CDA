import PyPDF2
import os
# pathlib

nb_global = 0

config = ["arrêté", "portant", "dérogation", "destruction", "animale", "protégées"]

index_loop = 1

match = []
total_matches = 0

matches_detail = {
    "arrêté": 0,
    "portant": 0,
    "dérogation": 0, 
    "destruction": 0, 
    "animale": 0, 
    "protégées": 0
}

for file in os.listdir("bouches_du_rhone_2019"):

    pdfFileObj = open('bouches_du_rhone_2019/' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.getOutlines)
    numPages = pdfReader.numPages

    for x in range(numPages):
        page = pdfReader.getPage(x).extractText()

        for item in config:

            if (item in page.lower()):
                match.append(item)
                total_matches += 1
                matches_detail[item] += 1

        #if match != []:
            #print("Fichier n°{} - Page n°{} - Nb occurences {}".format(index_loop, x, match))

        match = []

    index_loop = index_loop + 1

print("")
print("")
print("Il y a eu au total {} matchs.".format(total_matches))
print("")
print("")
print("La population des matchs par rapport aux mots clés est :")
print("")
print(matches_detail)
print("")
print("")



# loop sur chaque phrase:
#    si phrase commence par Arrêté:
#        alors match += 1