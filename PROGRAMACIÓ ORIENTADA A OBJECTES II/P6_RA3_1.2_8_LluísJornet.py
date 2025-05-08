# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Alumne amb edat controlada.
# Nom del document: activitat_8
# ----------------------------------------

class Alumne:
    def __init__(self):
        self.__edat = 0

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
