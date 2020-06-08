import os

path = 'D:\\projet\\github\\CDA\\thomas\\bot'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

# for f in files:
#     print(f)


def getAllPdf (path , extention = '.pfd'):
    '''
    path = la variable du chemin ou l'on veut cherhcer les pdf 
    extention = la variable qui selection 'lextention rechercher par default PDF
    return une liste de path vers des pdf a partir de la racine (C:)
    '''
    
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if extention in file:
                files.append(os.path.join(r, file))
    return(files)

print(getAllPdf(path))