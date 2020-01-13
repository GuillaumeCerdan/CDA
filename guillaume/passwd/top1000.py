from itertools import product
import time
import hashlib


def convertToMD5(str):
    result = hashlib.md5()
    result.update(str.encode("utf-8"))
    result.digest()
    return result.hexdigest()

with open("hachis.txt", encoding="UTF-8") as file:
    data = file.read()
    hachis = set(data.split('\n'))

with open("top1000pdwz.txt", encoding="UTF-8") as file:
    data = file.read()
    pdwz = set(data.split('\n'))

# chars = "azertyuiopqsdfghjklmwxcvbn"

start_time = time.time()

i=0

for p in pdwz:
    # if convertToMD5(''.join(p.lower())) in hachis:
    if convertToMD5(''.join(p)) in hachis:
        i+=1
        print(str(p))

print("--- %s seconds ---" % (time.time() - start_time))

print(i)

#product(chars,repeat = 4)