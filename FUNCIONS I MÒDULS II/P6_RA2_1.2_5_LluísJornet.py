# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Llegeix i escriu en un fitxer (mode r+).
# Nom del document: ex5_llegir_escriure
# ----------------------------------------

with open("sortida.txt", "r+") as f:
    print(f.read())
    f.write("Línia nova afegida al final\n")