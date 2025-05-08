# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Usuari amb gestió de contrasenya segura.
# Nom del document: activitat_4
# ----------------------------------------

class Usuari:
    def __init__(self):
        self.__contrasenya = ""

    def canviar_contrasenya(self, nova):
        if len(nova) >= 8:
            self.__contrasenya = nova

    def verificar_contrasenya(self, clau):
        return clau == self.__contrasenya
