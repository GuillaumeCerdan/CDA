import itertools 
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


# 
# liste_2 = [mot for mot in mylist if distance.nlevenshtein(mot, "arrêté", method=1) < 0.4]
# print("le mot : " + str(liste_2))

# print (liste_2)
# if mot in mydata:
#     print("il y est")


listemot= []
mot = ["c", "h", "i", "e", "n"]
for obj in itertools.permutations(mot):
    liste = list(obj)
    listemot.append("".join(liste))
    print (liste)
print (listemot)
alphabet = 'a z e r t y u i o p q s d f g h j k l m w x c v b n'
tabalpha = alphabet.split(sep=" ")
print (tabalpha)
i = 0 
for j in range (5,7):
    for obj in itertools.permutations(tabalpha,j):
        i+=1
print (i)



# input()