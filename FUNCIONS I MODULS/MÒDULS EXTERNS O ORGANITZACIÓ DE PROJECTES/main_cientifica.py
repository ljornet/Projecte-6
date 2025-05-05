# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa permet a l'usuari escollir una operació científica de les disponibles.
# Nom del document: main_cientifica
# ----------------------------------------

# Importem el mòdul científic
from cientifica import arrel_quadrada, sin_en_graus, potencia
from calculadora import suma, resta, multiplicacio, divisio

# Funció per mostrar el menú
def mostrar_menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Arrel quadrada")
    print("6. Sin (en graus)")
    print("7. Potència")
    opcio = int(input("Selecciona una opció (1-7): "))
    return opcio

# Funció per realitzar les operacions
def realitzar_operacio(opcio):
    if opcio == 1:
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        print(f"La suma és: {suma(a, b)}")
    elif opcio == 2:
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        print(f"La resta és: {resta(a, b)}")
    elif opcio == 3:
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        print(f"La multiplicació és: {multiplicacio(a, b)}")
    elif opcio == 4:
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        if b != 0:
            print(f"La divisió és: {divisio(a, b)}")
        else:
            print("No es pot dividir per zero.")
    elif opcio == 5:
        x = float(input("Introdueix el número per calcular l'arrel quadrada: "))
        print(f"L'arrel quadrada de {x} és: {arrel_quadrada(x)}")
    elif opcio == 6:
        angle = float(input("Introdueix l'angle en graus: "))
        print(f"El sin de {angle} graus és: {sin_en_graus(angle)}")
    elif opcio == 7:
        base = float(input("Introdueix la base: "))
        exponent = float(input("Introdueix l'exponent: "))
        print(f"{base} elevat a {exponent} és: {potencia(base, exponent)}")
    else:
        print("Opció no vàlida.")

# Executar el menú
opcio = mostrar_menu()
realitzar_operacio(opcio)
