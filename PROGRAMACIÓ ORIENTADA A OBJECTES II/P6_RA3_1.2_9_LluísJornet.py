# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Joc per gestionar la puntuació.
# Nom del document: activitat_9
# ----------------------------------------

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        self.__puntuacio += punts

    def reiniciar(self):
        self.__puntuacio = 0

    def obtenir_puntuacio(self):
        return self.__puntuacio
