entrada = input()

v = entrada.split(" ")

a = int(v[0])
b = int(v[1])
c = int(v[2])

ordenados = []
ordenados.append(a)
ordenados.append(b)
ordenados.append(c)
ordenados.sort()

for x in range(3):
    print(ordenados[x])
print("")
print(a)
print(b)
print(c)
