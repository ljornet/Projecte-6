# Classe de notificació per email
class EmailNotificador:
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

# Exemple d’una altra classe de notificació (opcional)
class SMSNotificador:
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

# Classe Comanda amb injecció de dependències
class Comanda:
    def __init__(self, client, notificador):  # Aquí li passem el notificador des de fora
        self.client = client
        self.notificador = notificador

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")
