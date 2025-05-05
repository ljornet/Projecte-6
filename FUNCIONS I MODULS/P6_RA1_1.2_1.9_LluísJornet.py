# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat determina l’estat d’una persona segons l’edat.
# Nom del document: activitat_9
# ----------------------------------------

def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Encara ets jove, gaudeix!"
    elif edat < 65:
        return "Adult", "Et trobes en edat laboral."
    else:
        return "Jubilat", "Temps per descansar i fer el que t'agrada."

for edat in [12, 25, 70]:
    estat, descripcio = estat_persona(edat)
    print(f"Edat: {edat} -> Estat: {estat} - {descripcio}")
