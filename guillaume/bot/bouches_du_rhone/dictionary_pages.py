import PyPDF2
import os

iterator = 0
nb_iteration = 0
nb_global = 0

for file in os.listdir("bouches_du_rhone_2019"):

    print("\n")

    suivi = {}

    # if (nb_iteration == 20):
    #     break

    pdfFileObj = open('bouches_du_rhone_2019/' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages

    iterator += numPages
    nb_environnement = 0

    for x in range(numPages):
        page = pdfReader.getPage(x).extractText()
        if ("environnement" in page):
            suivi[x] = suivi.get(x, 0) + page.count("environnement")
            nb_environnement += page.count("environnement")
            nb_global += page.count("environnement")
    
    nb_iteration += 1

    print(suivi)
    print(" -- En tout il y en a eu {}".format(nb_environnement))
    print("_" * 40)
    print("\n")

print("Sur tous les fichiers, on a trouvé {} occurences".format(nb_global))
print("Il y a donc en moyenne {} fois 'environnement' dans tous les fichiers".format(nb_global / nb_iteration))