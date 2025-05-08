# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe Estudiant amb una nota protegida i mètodes per gestionar-la.
# Nom del document: activitat_2
# ----------------------------------------

class Estudiant:
    def __init__(self):
        self._nota = 0

    def llegir_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
