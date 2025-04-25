# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat demana el nombre de minuts i els converteix a hores i minuts.
# Nom del document: activitat_20
# ----------------------------------------

# Demanem el nombre de minuts
minuts = int(input("Quants minuts vols convertir? "))

# Calculem les hores i els minuts restants
hores = minuts // 60
minuts_restants = minuts % 60

# Mostrem el resultat
print("El temps és: ", hores, "hores i", minuts_restants, "minuts")