# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat comprova si diferents nombres són parells.
# Nom del document: activitat_4
# ----------------------------------------

def es_parell(numero):
    return numero % 2 == 0

llista = [1, 2, 3, 4, 5, 6]
for num in llista:
    print(f"El número {num} és parell: {es_parell(num)}")
