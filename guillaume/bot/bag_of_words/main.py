sentence = """Un robot ne peut blesser un être humain ni, par son inaction, permettre qu'un humain soit blessé.
Un robot doit obéir aux ordres donnés par les êtres humains, sauf si de tels ordres sont en contradiction avec la Première Loi.
Un robot doit protéger sa propre existence aussi longtemps qu'une telle protection n'est pas en contradiction avec la Première et/ou la Deuxième Loi."""

split_by_space = sentence.split()
dictionary = {mot: split_by_space.count(mot) for mot in set(split_by_space)}

dictionary_sorted = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
print("Mon dictionnaire : {}".format(dictionary_sorted))