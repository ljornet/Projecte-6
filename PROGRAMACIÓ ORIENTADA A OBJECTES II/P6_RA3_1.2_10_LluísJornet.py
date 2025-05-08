# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquesta activitat crea una classe CompteUsuari amb validació d'email.
# Nom del document: activitat_10
# ----------------------------------------

class CompteUsuari:
    def __init__(self):
        self.__email = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
