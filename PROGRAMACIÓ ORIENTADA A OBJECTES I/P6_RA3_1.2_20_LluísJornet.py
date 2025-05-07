
from P6_RA3_1.2_3_LluísJornet import Persona

def mostrar_majors(persones):
    for p in persones:
        if p.edat > 30:
            p.presentar_se()

llista = [Persona("Albert", 25), Persona("Maria", 35), Persona("Joan", 40)]
mostrar_majors(llista)
