i = int(input())
j = int(input())
maior = 0
menor = 0

if i>j:
    maior = i
    menor = j

else:
    maior = j
    menor = i
soma = 0

for x in range(menor,maior+1):
    if x%13 != 0:
        soma = soma + x
print(soma)
