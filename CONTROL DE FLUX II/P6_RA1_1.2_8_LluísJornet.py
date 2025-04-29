# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per comptar quantes vocals hi ha en una frase.
# Nom del document: activitat_8
# ----------------------------------------

frase = input("Introdueix una frase: ").lower()
vocales = "aeiou"
conta_vocales = sum(1 for char in frase if char in vocales)
print(f"La frase conté {conta_vocales} vocals.")
