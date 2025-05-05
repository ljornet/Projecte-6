# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest mòdul conté funcions per realitzar operacions bàsiques: suma, resta, multiplicació i divisió.
# Nom del document: calculadora
# ----------------------------------------

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divideix(a, b):
    if b != 0:
        return a / b
    else:
        return "No es pot dividir per 0"
