# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per demanar una nota del 1 al 10 i mostrar si està aprovada o suspesa.
# Nom del document: activitat_4
# ----------------------------------------

# Demanem una nota i la convertim a enter
nota = int(input("Introdueix una nota del 1 al 10: "))

# Comprovem si la nota està aprovada (5 o més)
if nota >= 5 and nota <= 10:
    print("Aprovat")
elif nota >= 0 and nota < 5:
    print("Suspès")
else:
    print("Nota fora de rang. Ha de ser entre 0 i 10.")
