# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per comparar dues edats i mostrar quina és més gran o si són iguals.
# Nom del document: activitat_10
# ----------------------------------------

# Demanem una primera edat a l'usuari
edat1 = int(input("Donem una edat:"))

# Demanem una segona edat a l'usuari
edat2 = int(input("Donem una altra edat:"))

# Comprovem quina edat és més gran
if (edat1 < edat2):
    print("La edat mes gran es:", edat2)

# Comprovem si les dues edats són iguals
elif (edat1 == edat2):
    print("Les edats son iguals")

# Si cap de les dues condicions anteriors es compleix, la primera edat és la més gran
else:
    print("La edat mes gran es:", edat1)
