# pip install spacy
# Puis : python -m spacy download fr_core_news_sm
# https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/


import spacy

nlp = spacy.load("fr_core_news_md")

test = "Arrêté n°479 portant sur la déforestation en milieu rurales"

# Retourne tokens (mots)
def return_token(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc]

# Retourne ligne à ligne
def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

# Reconnaissance d'entités nommées
def entites_nommees(sentence):
    doc = nlp(sentence)
    return [(X.text, X.label_) for X in doc.ents]

# Retourne l'étiquetage morph-syntaxique
def morpho_syntaxique(sentence):
    doc = nlp(sentence)
    return [(X, X.pos_) for X in doc]



print(return_token(test))
print(morpho_syntaxique(test))