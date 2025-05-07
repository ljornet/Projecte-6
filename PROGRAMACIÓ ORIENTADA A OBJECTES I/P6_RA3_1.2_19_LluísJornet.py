
from P6_RA3_1.2_7_LluísJornet import Cercle

cercles = [Cercle(3), Cercle(5), Cercle(1)]

for c in cercles:
    if c.area() > 50:
        print(f"Cercle amb radi {c.radi} té àrea {c.area()}")
