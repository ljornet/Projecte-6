# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 2 - Comptar quantes vocals conté una frase
# Nom del document: activitat_2
# ----------------------------------------

frase = input("Escriu una frase: ")
vocal_count = sum(1 for lletra in frase.lower() if lletra in "aeiou")
print("Nombre de vocals:", vocal_count)