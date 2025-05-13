# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa crea una classe Llibre i les seves subclasses LlibrePaper i LlibreDigital.
# Nom del document: biblioteca
# ----------------------------------------

# Classe Llibre
class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

# Subclasse LlibrePaper amb atribut n_pàgines
class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pàgines):
        super().__init__(titol, autor)
        self.n_pàgines = n_pàgines

    def mostrar_info(self):
        print(f"Llibre en paper - Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pàgines}")

# Subclasse LlibreDigital amb atribut format
class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Llibre digital - Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")

# Proves
llibre_paper = LlibrePaper("La guerra dels móns", "H.G. Wells", 320)
llibre_digital = LlibreDigital("1984", "George Orwell", "PDF")

llibre_paper.mostrar_info()  # Llibre en paper - Títol: La guerra dels móns, Autor: H.G. Wells, Pàgines: 320
llibre_digital.mostrar_info()  # Llibre digital - Títol: 1984, Autor: George Orwell, Format: PDF
