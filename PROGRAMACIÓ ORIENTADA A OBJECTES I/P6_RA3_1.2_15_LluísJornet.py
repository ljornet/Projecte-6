
from P6_RA3_1.2_4_LluísJornet import Producte

def aplicar_descompte(productes):
    for p in productes:
        p.aplicar_descompte(10)

llista = [Producte("Ordinador", 1000), Producte("Ratolí", 25)]
aplicar_descompte(llista)
for p in llista:
    print(p.nom, p.preu)
