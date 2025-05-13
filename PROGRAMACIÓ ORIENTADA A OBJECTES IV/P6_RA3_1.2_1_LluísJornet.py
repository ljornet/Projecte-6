# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa mostra l'ús de la herència amb classes d'animals.
# Nom del document: animals
# ----------------------------------------

# Classe pare Animal
class Animal:
    def parlar(self):
        print("Aquest animal fa un so...")

# Subclasse Gos
class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

# Subclasse Gat
class Gat(Animal):
    def parlar(self):
        print("Miau!")

# Crear instàncies i provar
animal1 = Gos()
animal2 = Gat()

animal1.parlar()  # Bup bup!
animal2.parlar()  # Miau!