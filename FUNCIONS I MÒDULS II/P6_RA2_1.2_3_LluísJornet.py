# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Afegeix una línia a un fitxer existent sense esborrar el contingut anterior.
# Nom del document: ex3_afegir_fitxer
# ----------------------------------------

with open("sortida.txt", "a") as f:
    f.write("Quarta línia afegida\n")