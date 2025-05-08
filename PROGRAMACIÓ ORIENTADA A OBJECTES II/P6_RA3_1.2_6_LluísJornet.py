# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Producte amb preu controlat.
# Nom del document: activitat_6
# ----------------------------------------

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu if preu > 0 else 0

    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
