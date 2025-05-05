# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Filtra els nombres parells d'una llista
# Nom del document: funcio_filtra_parells
# ----------------------------------------

# Funció que rep una llista i retorna només els nombres parells
def filtra_parells(llista):
    return [n for n in llista if n % 2 == 0]