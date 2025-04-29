# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per comprovar si un número és primer.
# Nom del document: activitat_5
# ----------------------------------------

num = int(input("Introdueix un número enter positiu: "))
es_primer = True

if num < 2:
    es_primer = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primer = False
            break

if es_primer:
    print(f"{num} és un nombre primer.")
else:
    print(f"{num} no és un nombre primer.")
