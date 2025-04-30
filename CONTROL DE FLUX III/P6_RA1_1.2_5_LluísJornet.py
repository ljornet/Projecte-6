# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Mostra tots els nombres primers de 2 fins al número introduït.
# Nom del document: exercici_5
# ----------------------------------------

# Funció per saber si un número és primer
def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    # Demanem un enter positiu
    n = int(input("Introdueix un nombre enter positiu: "))

    # Comprovem que sigui major o igual a 2
    if n < 2:
        raise ValueError("El número ha de ser com a mínim 2.")

    # Imprimim els nombres primers de 2 fins a n
    print(f"Nombres primers de 2 fins a {n}:")
    for i in range(2, n + 1):
        if es_primer(i):
            print(i, end=" ")

except ValueError as e:
    # Gestionem l’error si no és un enter positiu vàlid
    print(f"Error: {e}")
