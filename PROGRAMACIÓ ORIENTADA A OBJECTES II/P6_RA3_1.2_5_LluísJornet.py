# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Sensor amb valor limitat entre 0 i 100.
# Nom del document: activitat_5
# ----------------------------------------

class Sensor:
    def __init__(self):
        self.__valor = 0

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
