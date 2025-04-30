# ----------------------------------------
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Activitat 20 - Filtrar paraules que comencen per vocal
# Nom del document: activitat_20
# ----------------------------------------

paraules2 = input("Escriu paraules separades per espais: ").split()
vocals = [p for p in paraules2 if p[0].lower() in "aeiou"]
print("Paraules que comencen per vocal:", vocals)