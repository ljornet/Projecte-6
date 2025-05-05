# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest mòdul conté funcions per validar correus electrònics i números de telèfon.
# Nom del document: validacions
# ----------------------------------------

import re

# Funció per validar un email
def es_email_valid(email):
    # Comprovem si el format de l'email és vàlid (usant una expressió regular)
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron_email, email))

# Funció per validar un número de telèfon (format bàsic per telèfons nacionals)
def es_telefon_valid(telefon):
    # Comprovem si el número de telèfon és vàlid (format bàsic de 9 xifres)
    patron_telefon = r'^[0-9]{9}$'
    return bool(re.match(patron_telefon, telefon))
