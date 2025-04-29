# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per demanar una lletra i dir si és una vocal o una consonant.
# Nom del document: activitat_6
# ----------------------------------------

# Demanem una lletra a l'usuari
lletra = input("Introdueix una lletra: ").lower()

# Comprovem si realment és una sola lletra
if len(lletra) != 1 or not lletra.isalpha():
    print("Has d'introduir només una lletra!")
elif lletra in "aeiou":
    print("És una vocal.")
else:
    print("És una consonant.")