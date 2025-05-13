# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa simula el moviment de diferents vehicles.
# Nom del document: transport
# ----------------------------------------

# Classe base Vehicle
class Vehicle:
    def moure(self):
        raise NotImplementedError("Aquest mètode ha de ser sobreescrit per les subclasses.")

# Subclasse Cotxe
class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe es mou per la carretera.")

# Subclasse Bicicleta
class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta es mou pedalant.")

# Subclasse Barca
class Barca(Vehicle):
    def moure(self):
        print("La barca es mou per l'aigua.")

# Funció per simular el moviment de tots els vehicles
def simular_moviment(vehicles):
    for vehicle in vehicles:
        vehicle.moure()

# Llista de vehicles
vehicles = [Cotxe(), Bicicleta(), Barca()]

# Simulem el moviment
simular_moviment(vehicles)