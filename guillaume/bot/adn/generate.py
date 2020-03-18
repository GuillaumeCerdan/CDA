# import random
# chars = ["A", "C", "T", "G"]
# combstart = ["A", "T", "G"]
# combend = [["T", "A", "A"], ["T", "A", "G"], ["T", "G", "A"]]
# brin = []
# for i in range(100):
#     temp = []
#     for j in range(3):
#         temp.append(random.choice(chars))
#     if (temp not in combstart) and (temp not in combend):
#         brin.append(temp)
# randstartidx = random.randint(25, 50)
# randendidx = random.randint(50, 75)
# randend = random.choice(combend)
# brin[randstartidx] = combstart
# brin[randendidx] = randend
# print("Mon brin : {}".format(brin))


toto = [1, 2, [3, 4], [5, [6, 7, [8, [9, 10, 11, [12, 13]]]]]]
wholelist = []

def unwrap(mylist):
    temp = []
    for element in mylist:
        if (not isinstance(element, list)):
            wholelist.append(element)
        else:
            for elem in element:
                temp.append(elem)
    if temp:
        unwrap(temp)

unwrap(toto)
print(wholelist)