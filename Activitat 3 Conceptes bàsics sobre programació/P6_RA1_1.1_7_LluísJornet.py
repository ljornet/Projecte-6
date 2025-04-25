# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat és per crear una calculadora que permet fer restes, multiplicacions i divisions amb dos variables.
# Nom del document: Activitat_7
# ----------------------------------------

print("Operacions disponibles:")
print("1. Resta")
print("2. Multiplicació")
print("3. Divisió")

operacio = input("Tria l'operació (1/2/3): ")

num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

if operacio == "1":
    print("El resultat de la resta és:", num1 - num2)
elif operacio == "2":
    print("El resultat de la multiplicació és:", num1 * num2)
elif operacio == "3":
    if num2 != 0:
        print("El resultat de la divisió és:", num1 / num2)
    else:
        print("NO es pot dividir per zero!")
else:
    print("Operació no vàlida!")
