# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa fa servir el paquet utilitats per realitzar conversió de temps i moneda.
# Nom del document: main_utilitats
# ----------------------------------------

# Importem les funcions des del paquet utilitats
from utilitats import temps, moneda

# Utilitzem les funcions del mòdul temps
segons = 3600
print(f"{segons} segons són {temps.segons_a_minuts(segons)} minuts.")
print(f"{segons} segons són {temps.segons_a_hores(segons)} hores.")

# Utilitzem les funcions del mòdul moneda
euros = 100
print(f"{euros} euros són {moneda.euros_a_dolares(euros)} dòlars.")
dolars = 110
print(f"{dolars} dòlars són {moneda.dolars_a_euros(dolars)} euros.")
