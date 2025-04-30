# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Mostra la taula de multiplicar d’un número introduït per l’usuari.
# Nom del document: exercici_3
# ----------------------------------------

try:
    # Demanem un número
    num = int(input("Introdueix un nombre enter per mostrar la seva taula de multiplicar: "))

    # Mostrem la taula del número de l’1 al 10
    print(f"Taula de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    # Gestionem l’error si no és un enter
    print("Error: Has d'introduir un nombre enter.")
