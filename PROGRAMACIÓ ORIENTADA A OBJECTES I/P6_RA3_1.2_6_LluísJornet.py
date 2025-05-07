
class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat

    def veure_saldo(self):
        return self.saldo
