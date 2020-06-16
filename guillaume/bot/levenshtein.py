import distance
from itertools import permutations



# AVEC LAMBDA
# with open('liste_francais.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#     mylist = data.split('\n')

# def getLast(mot):
#     return mot[len(mot) - 1]

# data = [mot for mot in mylist if len(mot > 3)]

# print(sorted(data, key = lambda mot: mot[2]))
# print(sorted(mylist, key = getLast))

# liste_2 = [mot for mot in mylist if distance.nlevenshtein(mot, "arrêté", method=1) < 0.5]
# print("le mot : " + str(liste_2))



# CREE LES ANAGRAMMES
my_mot = ["c", "h", "i", "e", "n"]

for mot in permutations(my_mot):
    print("".join(list(mot)))











# if mot in mydata:
#     print("il y est")



# TROUVE LES ANAGRAMMES
# my_mot = ["c", "h", "i", "e", "n"]
# my_mot_sorted = sorted(my_mot)

# for mot in mylist:
#     if (len(mot) != len(my_mot_sorted)):
#         mylist.remove(mot)

# for mot in mylist:
#     if sorted(mot) == my_mot_sorted:
#         print(mot)