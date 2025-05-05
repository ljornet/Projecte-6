# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Obre un fitxer en mode lectura o el crea si no existeix.
# Nom del document: ex9_crear_si_no_existeix
# ----------------------------------------

try:
    with open("auto.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    with open("auto.txt", "w") as f:
        f.write("Fitxer creat automàticament\n")
    print("Fitxer creat.")