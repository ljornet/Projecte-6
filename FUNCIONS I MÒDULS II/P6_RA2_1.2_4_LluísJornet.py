# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Compta el nombre de línies d’un fitxer.
# Nom del document: ex4_comptar_linies
# ----------------------------------------

with open("sortida.txt", "r") as f:
    linies = f.readlines()
    print("Nombre de línies:", len(linies))