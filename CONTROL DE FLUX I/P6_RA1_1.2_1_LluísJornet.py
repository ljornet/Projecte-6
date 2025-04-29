# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per comprovar si un número és més gran, més petit o igual a zero.
# Nom del document: activitat_1
# ----------------------------------------

# Demanem un número a l'usuari i el convertim a enter
num1 = int(input("Disme un número: "))

# Comprovem si el número és més gran que zero
if num1 > 0:
    print("És més gran que zero")

# Comprovem si és més petit que zero
elif num1 < 0:
    print("És més petit que zero")

# Si no és ni més gran ni més petit, és igual a zero
else:
    print("És igual a zero")