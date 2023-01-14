soma = 0
positivos = 0
for i in range (6):
    n = float(input())
    if n>0:
        soma = soma + n
        positivos+= 1

media = soma/positivos

print("%d valores positivos"%positivos)
print("%.1f"%media)
