
from P6_RA3_1.2_9_LluísJornet import Llibre

class Biblioteca:
    def __init__(self):
        self.llibre_list = []

    def afegir_llibre(self, llibre):
        self.llibre_list.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibre_list:
            llibre.mostrar_info()

b = Biblioteca()
b.afegir_llibre(Llibre("1984", "Orwell", 1949))
b.afegir_llibre(Llibre("El Petit Príncep", "Exupéry", 1943))
b.mostrar_llibres()
