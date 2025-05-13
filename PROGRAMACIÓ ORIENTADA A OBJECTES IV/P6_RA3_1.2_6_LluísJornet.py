# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa demostra el polimorfisme amb la classe Animal i les seves subclasses Gat i Vaca.
# Nom del document: sons_animals
# ----------------------------------------

# Classe base Animal
class Animal:
    def fer_soroll(self):
        raise NotImplementedError("Aquest mètode ha de ser sobreescrit per les subclasses.")

# Subclasse Gat
class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

# Subclasse Vaca
class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

# Funció que fa sonar l'animal
def reproduir_soroll(animal):
    print(animal.fer_soroll())

# Crear instàncies de Gat i Vaca
gat = Gat()
vaca = Vaca()

# Cridar la funció reproduir_soroll
reproduir_soroll(gat)   # Miau
reproduir_soroll(vaca)  # Muuu
