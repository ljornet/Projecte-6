
from P6_RA3_1.2_6_LluísJornet import CompteBancari

compte = CompteBancari()
compte.ingressar(100)
print("Saldo:", compte.veure_saldo())

compte.retirar(30)
print("Saldo:", compte.veure_saldo())

compte.retirar(100)
print("Saldo:", compte.veure_saldo())
