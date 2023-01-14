from math import inf
salary = float(input())

ajuste = 0

salarios = [inf, 2000 , 1200, 800 , 400]

ajustes = [4 , 7 , 10 , 12 , 15]

for x in range(5):
    if salary<= salarios[x]:
        ajuste = ajustes[x]

new = salary + (ajuste/100 * salary)
reaj = ajuste/100 * salary

print("Novo salario: %.2f"%new)
print("Reajuste ganho: %.2f"%reaj)
print("Em percentual:",ajuste,"%")