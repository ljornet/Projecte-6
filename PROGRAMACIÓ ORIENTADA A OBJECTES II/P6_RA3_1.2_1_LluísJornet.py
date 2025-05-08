# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe CompteBancari amb mètodes per gestionar el saldo.
# Nom del document: activitat_1
# ----------------------------------------

class CompteBancari:
    def __init__(self):
        self.__saldo = 0

    def ingressar(self, quantitat):
        self.__saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.__saldo:
            self.__saldo -= quantitat

    def consultar_saldo(self):
        return self.__saldo