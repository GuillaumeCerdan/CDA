import os
import sys
import fileinput
import csv 

fileToSearch = 'departments.csv'
tempFile = open( fileToSearch, 'r' )
listdep = []
listurl = []
for line in fileinput.input( fileToSearch):
    ##print(line)
    listdep.append(line)
    *_ , ville = line.split(',')
    ##ville = ville[:-1]
    ville = ville[:-1].replace(' ','-')
    ##ville = ville.strip('"')
    listurl.append(ville.strip('"')+".gouv.fr")
    
    

##listdep.pop(0)
####print (listdep)
##for i in listdep:
##    ##print (i)
##    *_ , ville = i.split(',')
##    ville = ville[:-1]
##    ville = ville.replace(' ','-')
##    listurl.append(ville+".gouv.fr")
    

listurl.pop(0)
print (listurl)       
input('\n press enter')
