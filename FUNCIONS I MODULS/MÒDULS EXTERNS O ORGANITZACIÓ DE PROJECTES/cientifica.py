# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest mòdul combina funcions bàsiques de càlcul amb funcions científiques del mòdul math.
# Nom del document: cientifica
# ----------------------------------------

import math
from calculadora import suma, resta, multiplicacio, divisio

# Funció per calcular la arrel quadrada
def arrel_quadrada(x):
    return math.sqrt(x)

# Funció per calcular el sen (sin) d'un angle en graus
def sin_en_graus(angle):
    return math.sin(math.radians(angle))

# Funció per calcular l'exponent
def potencia(base, exponent):
    return math.pow(base, exponent)
