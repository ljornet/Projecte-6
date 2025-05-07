
from P6_RA3_1.2_5_LluísJornet import Estudiant

llista = [Estudiant("Anna", 7), Estudiant("Marc", 4), Estudiant("Júlia", 9)]

for estudiant in llista:
    if estudiant.ha_aprovat():
        print(estudiant.nom)
