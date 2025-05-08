# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Termostat amb temperatura controlada entre 10 i 30 graus.
# Nom del document: activitat_3
# ----------------------------------------

class Termostat:
    def __init__(self):
        self.__temperatura = 20

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
