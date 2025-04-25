# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat demana a l'usuari quants dies té de vacances i calcula quantes hores són en total.
# Nom del document: activitat_17
# ----------------------------------------

# Demanem el nombre de dies de vacances
dies_vacances = int(input("Quants dies tens de vacances? "))

# Calculem les hores totals (suposant que cada dia té 24 hores)
hores_totals = dies_vacances * 24

# Mostrem el resultat
print("Tenint", dies_vacances, "dies de vacances, tens un total de", hores_totals, "hores.")
