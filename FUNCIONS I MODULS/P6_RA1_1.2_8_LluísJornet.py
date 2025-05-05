# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Calcula el factorial d'un nombre de forma recursiva
# Nom del document: funcio_factorial
# ----------------------------------------

# Funció recursiva que calcula el factorial d’un nombre
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
