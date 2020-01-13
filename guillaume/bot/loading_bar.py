from progress.bar import Bar
import time
from random import randint

print("Recherche de nouveaux recueils")
bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
    random_time = randint(1, 50) / 100
    time.sleep(random_time)
bar.finish()

print("2 nouveaux recueils trouvés !")
print("recueil_raa_no_12-2019-179_du_15_décembre_2019_-_tous_services.pdf")
print("recueil_raa_no_12-2019-180_du_16_décembre_2019_-_tous_services.pdf")
time.sleep(0.5)
print("Traiement de texte sur le recueil 1 trouvé")

for i in range(20):
    # Do some work
    bar.next()
    random_time = randint(1, 50) / 100
    time.sleep(random_time)
bar.finish()


print("Traiement de texte sur le recueil 2 trouvé")

for i in range(20):
    # Do some work
    bar.next()
    random_time = randint(1, 50) / 100
    time.sleep(random_time)
bar.finish()

print("Le recueil : recueil_raa_no_12-2019-179_du_15_décembre_2019_-_tous_services.pdf contient 2 fois le mot 'ecologie'")