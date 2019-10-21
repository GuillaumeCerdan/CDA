import csv

with open('departments.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for idx, row in enumerate(spamreader):
        if (idx != 0):
            dep = row[4]
            if dep.startswith('"'):
                dep = dep[1:-1]
            url = "www." + dep.replace(" ", "-") + ".gouv.fr"
            print(url)

# f=open("depts2018.txt", "r")
# contents =f.read()
# line = ""
# for i in range(len(contents)):
#     line += contents[i]

# print(line.split('\t'))