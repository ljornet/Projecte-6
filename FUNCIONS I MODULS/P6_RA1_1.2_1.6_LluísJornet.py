# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat multiplica un conjunt de nombres.
# Nom del document: activitat_6
# ----------------------------------------

def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat

print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))
