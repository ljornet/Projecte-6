# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest mòdul simula llençar un dau i calcula la mitjana de diversos llançaments.
# Nom del document: random
# ----------------------------------------

import random

def llença_dau():
    return random.randint(1, 6)

def mitjana_llençaments(n):
    resultats = [llença_dau() for _ in range(n)]
    return sum(resultats) / len(resultats)
