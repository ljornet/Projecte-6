# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa crea una classe Figura i les seves subclasses Quadrat i Cercle.
# Nom del document: figura_geometrica
# ----------------------------------------

import math

# Classe Figura amb mètode area
class Figura:
    def area(self):
        print("Àrea no definida")

# Subclasse Quadrat amb mètode area
class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2  # Àrea del quadrat

# Subclasse Cercle amb mètode area
class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2  # Àrea del cercle

# Proves
quadrat = Quadrat(4)
cercle = Cercle(3)

print(f"Àrea del quadrat: {quadrat.area()}")  # 16
print(f"Àrea del cercle: {cercle.area()}")    # 28.274333882308138
