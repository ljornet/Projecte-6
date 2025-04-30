# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Genera una seqüència del 0 fins a un número donat per l’usuari.
# Nom del document: exercici_1
# ----------------------------------------

try:
    # Demanem un número a l’usuari
    final = int(input("Introdueix un nombre enter per generar una seqüència de 0 fins a aquest número: "))
    
    # Generem la seqüència amb range() i la mostrem
    for i in range(final + 1):
        print(i, end=" ")

except ValueError:
    # Gestionem l’error si no posa un enter
    print("Error: Has d'introduir un nombre enter.")
