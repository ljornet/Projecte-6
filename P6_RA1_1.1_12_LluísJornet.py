# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per calcular l'àrea d'un cercle a partir del seu radi.
# Nom del document: activitat_10
# ----------------------------------------

# Demanem a l'usuari que introdueixi el radi del cercle
radi = int(input("Radi del cercle: "))

# Assignem el valor de Pi (aproximat) a la variable 'Pl'
Pl = 3.14

# Calculem el radi al quadrat
radicuadrat = radi * radi

# Imprimim el resultat de l'àrea, multiplicant Pi pel radi al quadrat
print("L'àrea del cercle és:", Pl * radicuadrat)