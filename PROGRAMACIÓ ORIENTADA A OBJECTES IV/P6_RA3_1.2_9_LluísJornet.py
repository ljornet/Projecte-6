# ---------------------------------------- 
# Nom: Lluís
# Cognoms: Jornet Marimon
# Descripció del Programa: Aquest programa envia missatges utilitzant diferents canals de comunicació.
# Nom del document: missatgeria
# ----------------------------------------

# Classe base Missatger
class Missatger:
    def enviar(self, missatge):
        raise NotImplementedError("Aquest mètode ha de ser sobreescrit per les subclasses.")

# Subclasse Email
class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

# Subclasse SMS
class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

# Subclasse WhatsApp
class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")

# Funció per enviar missatges
def enviar_missatges(missatgers, missatge):
    for missatger in missatgers:
        missatger.enviar(missatge)

# Llista de missatgers
missatgers = [Email(), SMS(), WhatsApp()]

# Enviem el missatge
enviar_missatges(missatgers, "Hola! Aquest és un missatge.")