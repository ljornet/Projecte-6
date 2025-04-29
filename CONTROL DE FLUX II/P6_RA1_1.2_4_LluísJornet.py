# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per generar un número aleatori i fer que l'usuari l'endevini.
# Nom del document: activitat_5
# ----------------------------------------

import random

num_aleatori = random.randint(1, 100)
endivinat = False

while not endivinat:
    intent = int(input("Endevina el número entre 1 i 100: "))
    if intent < num_aleatori:
        print("Massa baix!")
    elif intent > num_aleatori:
        print("Massa alt!")
    else:
        print("Has encertat!")
        endivinat = True
