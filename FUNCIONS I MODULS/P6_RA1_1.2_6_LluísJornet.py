# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Multiplica qualsevol quantitat de nombres
# Nom del document: funcio_multiplica_tot
# ----------------------------------------

# Funció que multiplica tots els nombres rebuts
def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat