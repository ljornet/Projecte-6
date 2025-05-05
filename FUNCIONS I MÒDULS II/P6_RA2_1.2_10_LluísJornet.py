# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Llegeix un fitxer manualment i assegura que es tanqui fins i tot amb errors.
# Nom del document: ex10_tancar_fitxer_amb_error
# ----------------------------------------

f = None
try:
    f = open("missatge.txt", "r")
    contingut = f.read()
    print(contingut)
except Exception as e:
    print("Error durant la lectura:", e)
finally:
    if f:
        f.close()
        print("Fitxer tancat.")