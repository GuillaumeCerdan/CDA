import PyPDF2
import os

whole_number_pages = 0
nb_occurences = 0

whole_good_dictionary = {}
whole_dictionary = []

for file in os.listdir("bouches_du_rhone_2019"):

    suivi = {}

    pdfFileObj = open('bouches_du_rhone_2019/' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages

    whole_number_pages += numPages
    nb_environnement = 0

    for x in range(numPages):
        page = pdfReader.getPage(x).extractText()
        if ("environnement" in page):
            suivi["Page n°{}".format(x)] = suivi.get("Page n°{}".format(x), 0) + page.count("environnement")
            nb_environnement += page.count("environnement")
            nb_occurences += page.count("environnement")
    if nb_environnement > 0:
        whole_good_dictionary["Document : {}".format(file)] = suivi
    whole_dictionary.append(file)

# print("Sur tous les fichiers, on a trouvé {} occurences".format(nb_occurences))
# print("Il y a donc en moyenne {} fois 'environnement' dans tous les fichiers".format(nb_occurences / nb_iteration))
print("Voici la population {}".format(whole_good_dictionary)) 
print(whole_dictionary)