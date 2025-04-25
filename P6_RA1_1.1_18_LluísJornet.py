# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat calcula el sou mensual a partir del sou anual que introdueix l'usuari.
# Nom del document: activitat_18
# ----------------------------------------

# Demanem el sou anual
sou_anual = int(input("Quin és el teu sou anual? "))

# Calculem el sou mensual
sou_mensual = sou_anual / 12

# Mostrem el resultat (sense decimales)
print("El teu sou mensual és: ", sou_mensual, "€")
