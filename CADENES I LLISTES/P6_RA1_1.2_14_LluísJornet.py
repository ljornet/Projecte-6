# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 14 - Separar 10 números en parells i senars
# Nom del document: activitat_14
# ----------------------------------------

nums = []
parells = []
senars = []
for i in range(10):
    n = int(input(f"Introdueix el número {i+1}: "))
    nums.append(n)
    if n % 2 == 0:
        parells.append(n)
    else:
        senars.append(n)
print("Parells:", parells)
print("Senars:", senars)