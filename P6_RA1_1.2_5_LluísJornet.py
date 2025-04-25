# a. Una constant
EDAT_MINIMA_CONDUIR = 18

# c. Una entrada de l’usuari (fusionant input i int)
edat = int(input("Quina és la teva edat? "))

# b. Lògica condicional
if edat >= EDAT_MINIMA_CONDUIR:
  print("Pots conduir.")
elif edat == EDAT_MINIMA_CONDUIR - 1:
  print("Gairebé pots conduir! Falta un any.")
else:
  print("Encara no pots conduir.")