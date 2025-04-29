# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per calcular l'edat a partir de l'any de naixement i dir si ets major d'edat.
# Nom del document: activitat_5
# ----------------------------------------

# Importem la llibreria datetime per saber l'any actual
import datetime

# Demanem l'any de naixement a l'usuari
any_naixement = int(input("Introdueix el teu any de naixement: "))

# Obtenim l'any actual
any_actual = datetime.datetime.now().year

# Calculem l'edat
edat = any_actual - any_naixement

# Mostrem l'edat
print("Tens", edat, "anys.")

# Comprovem si és major, menor o si té just 18 (per fer servir elif)
if edat > 18:
    print("Ets major d'edat.")
elif edat == 18:
    print("Acabes de fer els 18! Ja ets major d'edat.")
else:
    print("No ets major d'edat.")