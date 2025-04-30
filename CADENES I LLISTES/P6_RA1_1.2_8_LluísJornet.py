# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 8 - Eliminar espais d'una cadena
# Nom del document: activitat_8
# ----------------------------------------

def elimina_espais(cadena):
    return cadena.replace(" ", "")

text2 = input("Escriu una cadena amb espais: ")
print("Sense espais:", elimina_espais(text2))
