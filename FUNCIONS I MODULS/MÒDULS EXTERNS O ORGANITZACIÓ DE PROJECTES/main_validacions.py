# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa prova les funcions de validació d'email i telèfon.
# Nom del document: main_validacions
# ----------------------------------------

# Importem el mòdul de validacions
from validacions import es_email_valid, es_telefon_valid

# Proves amb dades vàlides i no vàlides
emails = ["joan@domini.com", "joan@domini", "joan@com"]
telefonos = ["612345678", "61234", "abc123456"]

# Validem els emails
for email in emails:
    print(f"Email: {email} - Vàlid: {es_email_valid(email)}")

# Validem els números de telèfon
for telefon in telefonos:
    print(f"Telèfon: {telefon} - Vàlid: {es_telefon_valid(telefon)}")
