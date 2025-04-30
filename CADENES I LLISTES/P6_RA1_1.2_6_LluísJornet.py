# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 6 - Mostrar primera i última lletra d'una cadena
# Nom del document: activitat_6
# ----------------------------------------

cadena2 = input("Escriu una cadena: ")
if len(cadena2) > 0:
    print("Primera lletra:", cadena2[0])
    print("Última lletra:", cadena2[-1])
else:
    print("Cadena buida.")