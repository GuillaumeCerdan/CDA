import json

with open('file.txt', 'r', encoding="UTF-8") as file:

     RAA = (json.loads(file.read()))
     file.close() 

# try avec tt a 1 pt
for arrete in RAA:
    score = 0 
    # if "destruction" in RAA[arrete].lower():
    #     score +=.15
    # if "introdution" in RAA[arrete].lower():
    #     score +=.15
    # if "prelevement" in RAA[arrete].lower():
    #     score +=.2
    if "environement" in RAA[arrete].lower():
        # score += .35
        score += 1
    if "chasse" in RAA[arrete].lower():
        score += 1
        # score += .3
    if "animaux" in RAA[arrete].lower() or "animal" in RAA[arrete].lower():
        score += 1
        # score+= .5
    if "ACCA" in RAA[arrete]:
        score += 1
        # score+= .3
    # if "nuissible" in RAA[arrete].lower():
    #     score+=.05
    if "ONCFS" in RAA[arrete]:
        score += 1
        # score += .35
    if "louveterie" in RAA[arrete].lower():
        score += 1
        # score += .3
    if "gibier" in RAA[arrete].lower():
        score += 1
        # score += .3     
    if "faune sauvage" in RAA[arrete].lower() or "faune" in RAA[arrete].lower():
        score += 1
        # score += .2   