from tika import parser  # il faut java 7 ou plus (lourd)
from datetime import date
import os

# with open ('D:/projet/github/CDA/thomas/bot/echantillonTestPdf/Recueil_RAA_07-2019-001_03_janvier_2019.pdf',"rb")as file:
#     data = file.read
#     print(data)
#     file.close()


path = 'D:/projet/github/CDA/thomas/bot/echantillonTestPdf/'
mot = "environnement"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    name = f.split("/").pop()
    raw = parser.from_file(f)
    texte = str(raw['content'])
    retourtext = open(r"D:/projet/github/CDA/thomas/bot/echantillonTestPdftxt/" + name + '.txt',"a", encoding='UTF-8')
    retourtext.write('£££ lu avec tika le {}'.format(date.today()))

    retourtext.write(texte.strip())


    if (mot in texte.lower()):
        print ("il y a {} fois {}".format(texte.count(mot),mot))
        retourtext.write("\n \n il y a {} fois {}".format(texte.count(mot),mot))
    else :
        print("nop")


    retourtext.close()
    # os.startfile("D:/projet/github/CDA/thomas/bot/echantillonTestPdftxt/" + name + '.txt')
