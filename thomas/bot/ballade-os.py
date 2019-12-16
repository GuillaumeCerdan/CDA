import os

path = 'D:\\projet\\github\\CDA\\thomas\\bot'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)