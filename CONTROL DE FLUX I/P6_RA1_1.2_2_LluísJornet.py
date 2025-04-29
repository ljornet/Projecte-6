# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per saber si un número és parell o imparell.
# Nom del document: activitat_2
# ----------------------------------------

# Demanem un número a l'usuari i el convertim a enter
numero = int(input("Introdueix un número: "))

# Fem la comprovació si és parell (residu 0 al dividir per 2)
if numero % 2 == 0:
    print("El número és parell.")
else:
    print("El número és imparell.")
