# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per mostrar la taula de multiplicar d’un número donat per l’usuari.
# Nom del document: activitat_3
# ----------------------------------------

num = int(input("Introdueix un número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")