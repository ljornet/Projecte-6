# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Comprova si un fitxer existeix abans de llegir-lo.
# Nom del document: ex6_comprovar_existencia
# ----------------------------------------

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as f:
        print(f.read())
else:
    print("El fitxer dades.txt no existeix.")