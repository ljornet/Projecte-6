
class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}")
