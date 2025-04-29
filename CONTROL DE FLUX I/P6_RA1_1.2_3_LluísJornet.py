# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per demanar tres números i mostrar quin és el més gran.
# Nom del document: activitat_3
# ----------------------------------------

# Demanem tres números a l'usuari i els convertim a enters
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
num3 = int(input("Introdueix el tercer número: "))

# Fem servir la funció max() per saber quin és el més gran
mes_gran = max(num1, num2, num3)

# Mostrem el resultat
print("El número més gran és:", mes_gran)