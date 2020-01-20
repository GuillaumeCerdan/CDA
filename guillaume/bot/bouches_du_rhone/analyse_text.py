import PyPDF2
import os

iterator = 0
nb_global = 0
suivi = {}
for file in os.listdir("bouches_du_rhone_2019"):

    if (nb_iteration == 1):
        break

    pdfFileObj = open('bouches_du_rhone_2019/' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages

    iterator += numPages
    nb_environnement = 0
    for x in range(numPages):
        page = pdfReader.getPage(x).extractText()
        if ("environnement" in page):
            nb_environnement += 1
            suivi[x] = nb_environnement

    # if (nb_environnement > 0):
    #     print("Dans le fichier {}, nombre de fois que le mot environnement est trouvé {}".format(file, nb_environnement))
        
    # else:
    #     print("Il n'y en a pas dans le fichier {}".format(file))
    
    # print("\n")
    # print("_" * 30)
    # print("\n")

    

    # nb_global += nb_environnement

# print("Iterator : {}".format(iterator))
# print("Moyenne : {}".format(iterator / (309 - 85)))
# print("\n")
# print("\n")
# print("_" * 30)
# print("Il y a eu {} occurences du mot environnement".format(nb_global))
# print('\n')
print(suivi)