# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Escriu 3 línies en un fitxer, esborrant el contingut anterior.
# Nom del document: ex2_escriure_fitxer
# ----------------------------------------

with open("sortida.txt", "w") as f:
    f.write("Primera línia\nSegona línia\nTercera línia\n")
