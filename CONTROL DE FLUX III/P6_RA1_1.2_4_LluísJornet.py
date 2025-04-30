# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Mostra tots els nombres parells de 0 fins al número introduït.
# Nom del document: exercici_4
# ----------------------------------------

try:
    # Demanem un enter positiu
    n = int(input("Introdueix un nombre enter positiu: "))

    # Comprovem que sigui positiu
    if n < 0:
        raise ValueError("El número ha de ser positiu o zero.")

    # Imprimim els nombres parells de 0 fins a n
    print(f"Nombres parells de 0 fins a {n}:")
    for i in range(0, n + 1, 2):
        print(i, end=" ")

except ValueError as e:
    # Gestionem l’error si no és un enter positiu
    print(f"Error: {e}")
