n = int(input())

somas = []
soma = 0
for i in range(n):
    l = input()
    v = l.split(" ")
    x = int(v[0])
    y = int(v[1])

    if x>y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    soma = 0
    for j in range(menor+1,maior):
        if j%2 != 0:
            soma = soma + j
    somas.append(soma)

for z in range(n):
    print(somas[z])
