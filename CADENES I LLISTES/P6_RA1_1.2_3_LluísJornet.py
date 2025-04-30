# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 3 - Revertir una cadena
# Nom del document: activitat_3
# ----------------------------------------

def reversa(cadena):
    return cadena[::-1]

text = input("Escriu una cadena: ")
print("Revertida:", reversa(text))