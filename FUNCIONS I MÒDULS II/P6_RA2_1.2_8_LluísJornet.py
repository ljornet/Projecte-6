# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Llegeix enters d’un fitxer i ignora errors si alguna línia no és vàlida.
# Nom del document: ex8_fitxer_mal_format
# ----------------------------------------

with open("nombres.txt", "w") as f:
    f.write("12\nhola\n34\n5a\n78\n")

with open("nombres.txt", "r") as f:
    for i, linia in enumerate(f, 1):
        try:
            numero = int(linia)
            print(f"Línia {i}: {numero}")
        except ValueError:
            print(f"Error a la línia {i}: no és un enter vàlid.")
