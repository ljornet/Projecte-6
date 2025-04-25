# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per comprovar si un número introduït per l'usuari és parell o senar.
# Nom del document: Activitat_9
# ----------------------------------------

# Demanem un número a l'usuari
num1 = int(input("Donem un numero i et dire si es parell o senar:"))

# Comprovem si el número és divisible entre 2 (és a dir, si és parell)
if (num1 % 2 == 0):
    print("Es parell")
# Si no és divisible entre 2, és senar
else:
    print("Es senar")