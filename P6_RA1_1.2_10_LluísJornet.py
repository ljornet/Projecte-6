# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per crear una calculadora que permet fer sumes, restes, multiplicacions i divisions amb dos variables.
# Nom del document: Activitat_10
# ----------------------------------------

print("Operacions disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicació")
print("4. Divisió")

operacio = input("Tria l'operació (1/2/3/4): ")

num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

if operacio == "1":
    print("El resultat de la suma és:", num1 + num2)
elif operacio == "2":
    print("El resultat de la resta és:", num1 - num2)
elif operacio == "3":
    print("El resultat de la multiplicació és:", num1 * num2)
elif operacio == "4":
    if num2 != 0:
        print("El resultat de la divisió és:", num1 / num2)
    else:
        print("NO es pot dividir per zero!")
else:
    print("Operació no vàlida!")