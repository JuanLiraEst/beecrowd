numeros = []
inverso = []
for x in range(20):
    n = int(input())
    numeros.append(n)

x= 19

while x>=0:
    inverso.append(numeros[x])
    x-=1

print(numeros)
print(inverso)