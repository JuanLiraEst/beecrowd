numeros = []
ordenado = []
for x in range(100):
    n = int(input())
    numeros.append(n)
    ordenado.append(n)

ordenado.sort()

for x in range(100):
    if numeros[x] == ordenado[99]:
        print(x+1)

