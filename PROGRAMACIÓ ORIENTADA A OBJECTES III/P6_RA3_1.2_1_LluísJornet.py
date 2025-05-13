# Classe de la impressora PDF
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

# Classe de la impressora en paper
class ImpressoraPaper:
    def imprimir(self, contingut):
        print(f"Imprimint en paper: {contingut}")

# Classe Factura amb injecció de dependències
class Factura:
    def __init__(self, client, import_total, impressora):  # Aquí injectem la impressora
        self.client = client
        self.import_total = import_total
        self.impressora = impressora

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)
