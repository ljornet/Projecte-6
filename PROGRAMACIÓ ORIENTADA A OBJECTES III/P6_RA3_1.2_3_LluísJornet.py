# Classe que aplica un 20% de descompte
class Descompte20:
    def aplicar(self, total):
        return total * 0.2

# Classe del carret de la compra
class CarretCompra:
    def __init__(self, total, estrategia_descompte):
        self.total = total
        self.estrategia_descompte = estrategia_descompte

    def calcular_total_amb_descompte(self):
        descompte = self.estrategia_descompte.aplicar(self.total)
        return self.total - descompte
