# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa utilitza el polimorfisme per dibuixar diferents tipus de figures geomètriques.
# Nom del document: dibuixar_figures
# ----------------------------------------

# Classe base Figura
class Figura:
    def dibuixar(self):
        raise NotImplementedError("Aquest mètode ha de ser sobreescrit per les subclasses.")

# Subclasse Cercle
class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle.")

# Subclasse Quadrat
class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat.")

# Subclasse Triangle
class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle.")

# Llista de figures
figures = [Cercle(), Quadrat(), Triangle()]

# Recorrem la llista i cridem dibuixar() per cada figura
for figura in figures:
    figura.dibuixar()
