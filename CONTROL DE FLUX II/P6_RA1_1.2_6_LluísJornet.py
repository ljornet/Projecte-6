# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per mostrar els primers 10 termes de la seqüència de Fibonacci.
# Nom del document: activitat_6
# ----------------------------------------

fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print(fibonacci)
