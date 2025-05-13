# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa crea una classe Persona i una subclasse Treballador, demostrant l'herència.
# Nom del document: persones_treballadors
# ----------------------------------------

# Classe Persona
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

# Subclasse Treballador que hereta de Persona
class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)  # Crida al constructor de Persona
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")

# Crear una instància de Treballador i provar els mètodes
treballador1 = Treballador("Lluís", 20, "programador")
treballador1.saludar()         # Hola, sóc Lluís
treballador1.mostrar_feina()   # Treballo com a programador
