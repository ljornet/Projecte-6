# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa mostra la data i hora actual i calcula els dies restants per una data determinada.
# Nom del document: main_datetime
# ----------------------------------------

# Importem el mòdul datetime
import datetime

# Obtenim la data i hora actual
data_actual = datetime.datetime.now()

# Imprimim la data i hora actual en el format desitjat
print("Data i hora actual: ", data_actual.strftime("%d/%m/%Y %H:%M"))

# Data de Nadal (25 de desembre)
nadal = datetime.datetime(year=data_actual.year, month=12, day=25)

# Si ja hem passat Nadal aquest any, calculem els dies fins a Nadal de l'any següent
if data_actual > nadal:
    nadal = datetime.datetime(year=data_actual.year + 1, month=12, day=25)

# Calculem la diferència en dies
dies_fins_nadal = (nadal - data_actual).days

print(f"Falten {dies_fins_nadal} dies per Nadal.")