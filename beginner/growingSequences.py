numeros = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        numeros.append(x)

for x in range(len(numeros)):
    for y in range(numeros[x]):
        if y+1 == numeros[x]:
            print(y+1)
        else:
            print(y+1, end=" ")




