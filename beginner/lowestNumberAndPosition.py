n = int(input())

valores = input()

v = valores.split(" ")

numeros = []
ordenado = []
for x in range(n):
    numeros.append(int(v[x]))
    ordenado.append(int(v[x]))

ordenado.sort()
menor = ordenado[0]

posicao = 0
for x in range(n):
    if numeros[x] == menor:
        posicao = x

print("Menor valor: %d"%menor)
print("Posicao: %d"%posicao)

