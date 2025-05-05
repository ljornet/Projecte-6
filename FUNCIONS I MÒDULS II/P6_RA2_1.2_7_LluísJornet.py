# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Gestiona un error d'escriptura (PermissionError).
# Nom del document: ex7_gestionar_permissionerror
# ----------------------------------------

try:
    with open("resultats.txt", "w") as f:
        f.write("Escrivint resultats...\n")
except PermissionError:
    print("No tens permisos per escriure en aquest fitxer.")