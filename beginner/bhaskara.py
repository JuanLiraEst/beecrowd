from math import sqrt
valores = input()

v = valores.split(" ")

a = float(v[0])
b = float(v[1])
c = float(v[2])

delta = (b**2) - (4*a*c)

if a==0 or delta<0:
    print("Impossivel calcular")

else:
    x1 = (-b+sqrt(delta))/(2*a)
    x2 = (-b-sqrt(delta))/(2*a)

    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)
