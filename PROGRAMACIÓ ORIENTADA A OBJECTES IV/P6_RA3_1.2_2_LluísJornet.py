# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa mostra l'ús de la herència amb vehicles i cotxes.
# Nom del document: vehicles
# ----------------------------------------

# Classe pare Vehicle
class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"{self.marca} engegant...")

# Subclasse Cotxe
class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

# Crear instància i provar
cotxe1 = Cotxe("Toyota")
cotxe1.arrencar()        # Toyota engegant...
cotxe1.tocar_claxon()    # Pip pip!
