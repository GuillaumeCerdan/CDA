from tqdm import tqdm
import time
from random import randint

# Créé une Progress Bar
for i in tqdm(range(10)):
    val = randint(0,1)
    print(val)
    time.sleep(val)