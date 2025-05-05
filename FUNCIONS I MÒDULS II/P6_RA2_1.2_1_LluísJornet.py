# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Llegeix i mostra el contingut d’un fitxer de text.
# Nom del document: ex1_llegir_fitxer
# ----------------------------------------

with open("missatge.txt", "w") as f:
    f.write("Hola, món!")

with open("missatge.txt", "r") as f:
    contingut = f.read()
    print(contingut)