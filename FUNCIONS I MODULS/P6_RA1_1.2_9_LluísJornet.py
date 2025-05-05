# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Classifica una persona segons la seva edat i retorna una descripció
# Nom del document: funcio_estat_persona
# ----------------------------------------

# Funció que classifica una persona per edat i retorna un estat i una descripció
def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Encara ets jove, gaudeix!"
    elif edat < 65:
        return "Adult", "Et trobes en edat laboral."
    else:
        return "Jubilat", "Temps per descansar i fer el que t'agrada."