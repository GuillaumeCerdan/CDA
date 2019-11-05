import distance









# AVEC LAMBDA
# with open('liste_francais.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#     mylist = data.split('\n')

# def getLast(mot):
#     return mot[len(mot) - 1]

# data = [mot for mot in mylist if len(mot > 3)]

# print(sorted(data, key = lambda mot: mot[2]))
# print(sorted(mylist, key = getLast))





# TROUVE LES ANAGRAMMES
# my_mot = ["c", "h", "i", "e", "n"]
# my_mot_sorted = sorted(my_mot)

# for mot in mylist:
#     if (len(mot) != len(my_mot_sorted)):
#         mylist.remove(mot)

# for mot in mylist:
#     if sorted(mot) == my_mot_sorted:
#         print(mot)



# liste_2 = [mot for mot in mylist if distance.nlevenshtein(mot, "chien", method=1) < 0.3]
# print("le mot : " + str(liste_2))



# if mot in mydata:
#     print("il y est")