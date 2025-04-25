# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa calcula el preu d'un producte amb IVA afegit, donat el preu sense IVA.
# Nom del document: activitat_8
# ----------------------------------------

# Demanem el preu sense IVA
PreuSensIVA = int(input("Preu Sense Iva: "))

# Calculem el preu amb IVA
PreuAmbIVA = (PreuSensIVA * 1.21)

# Mostrem el resultat
print("El preu amb IVA és de: ", PreuAmbIVA)
