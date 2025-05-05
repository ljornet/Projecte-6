# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa utilitza el mòdul constants per calcular la força gravitatòria.
# Nom del document: main_constants
# ----------------------------------------

# Importem les constants
from constants import PI, GRAVETAT

# Suposarem que tenim una massa de 10 kg
massa = 10  # en kg

# Fórmula de la força gravitatòria: F = m * g
força = massa * GRAVETAT

print(f"La força gravitatòria sobre un objecte de {massa} kg és {força} N.")
