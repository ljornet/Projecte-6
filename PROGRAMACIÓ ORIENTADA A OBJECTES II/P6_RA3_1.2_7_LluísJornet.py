# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Rellotge amb hores controlades i format HH:00.
# Nom del document: activitat_7
# ----------------------------------------

class Rellotge:
    def __init__(self):
        self.__hores = 0

    def set_hores(self, hores):
        if 0 <= hores <= 23:
            self.__hores = hores

    def mostrar_hores(self):
        return f"{self.__hores:02d}:00"
