# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Calcula la suma dels nombres des de 1 fins al número introduït.
# Nom del document: exercici_2
# ----------------------------------------

try:
    # Demanem un número enter positiu
    n = int(input("Introdueix un nombre enter positiu per calcular la suma: "))
    
    # Comprovem que sigui positiu
    if n < 1:
        raise ValueError("El número ha de ser positiu.")

    # Calculem la suma de 1 fins a n amb range i sum
    suma = sum(range(1, n + 1))
    print(f"La suma de 1 fins a {n} és {suma}")

except ValueError as e:
    # Gestionem errors de valor no vàlid o negatiu
    print(f"Error: {e}")
