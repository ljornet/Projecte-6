# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 12 - Demanar 5 paraules i guardar-les en una llista
# Nom del document: activitat_12
# ----------------------------------------

paraules = []
for i in range(5):
    p = input(f"Escriu la paraula {i+1}: ")
    paraules.append(p)
print("Llista de paraules:", paraules)