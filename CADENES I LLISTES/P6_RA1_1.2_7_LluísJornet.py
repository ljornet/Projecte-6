# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 7 - Comptar quantes vegades apareix una lletra
# Nom del document: activitat_7
# ----------------------------------------

cadena3 = input("Escriu una cadena: ")
lletra = input("Quina lletra vols comptar?: ")
compte = cadena3.lower().count(lletra.lower())
print(f"La lletra '{lletra}' apareix {compte} cops.")