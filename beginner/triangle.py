l = input()

v = l.split(" ")

v1 = float(v[0])
v2 = float(v[1])
v3 = float(v[2])

numeros = []
numeros.append(v1)
numeros.append(v2)
numeros.append(v3)

numeros.sort()
c = numeros[0]
b = numeros[1]
a = numeros[2]

if b+c > a:
    perimetro = a+b+c
    print("Perimetro = %.1f"%perimetro)

else:
    area = (a+b)*c/2
    print("Area = %.1f"%area)
