# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat filtra els nombres parells d'una llista.
# Nom del document: activitat_10
# ----------------------------------------

def filtra_parells(llista):
    return [n for n in llista if n % 2 == 0]

print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))
