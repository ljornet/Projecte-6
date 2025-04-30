# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 4 - Verificar si una paraula és un palíndrom
# Nom del document: activitat_4
# ----------------------------------------

paraula = input("Escriu una paraula: ").lower()
if paraula == paraula[::-1]:
    print("És un palíndrom!")
else:
    print("No és un palíndrom.")