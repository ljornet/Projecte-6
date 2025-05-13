# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa calcula el sou de diferents tipus d'empleats.
# Nom del document: empleats_i_sous
# ----------------------------------------

# Classe base Empleat
class Empleat:
    def calcular_sou(self):
        raise NotImplementedError("Aquest mètode ha de ser sobreescrit per les subclasses.")

# Subclasse Fixe
class Fixe(Empleat):
    def calcular_sou(self):
        return 2000  # Sou fix

# Subclasse Autonom
class Autonom(Empleat):
    def calcular_sou(self):
        return 1500 + 0.1 * 5000  # Exemple de sou variable per un autònom

# Funció per mostrar els sous
def mostrar_sous(llista_empleats):
    for empleat in llista_empleats:
        print(f"Sou: {empleat.calcular_sou()} €")

# Creem una llista d'empleats
empleats = [Fixe(), Autonom()]

# Mostrem els sous
mostrar_sous(empleats)