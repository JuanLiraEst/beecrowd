total = float(input(""))

cem = int(total//100)
listado = cem*100

cinquenta = int((total-listado)//50)
listado = listado + cinquenta*50

vinte = int((total-listado)//20)
listado = listado + vinte*20

dez = int((total-listado)//10)
listado = listado + dez*10

cinco = int((total-listado)//5)
listado = listado + cinco*5

dois = int((total-listado)//2)
listado = listado + dois*2

um = int(total-listado)
listado = listado + um

cinqcent = int((total-listado)//0.5)
listado = listado + cinqcent*0.5

vintcinco = int((total-listado)//0.25)
listado = listado + vintcinco*0.25

dezcent = int((total-listado)//0.10)
listado = listado + dezcent*0.10

cincocent = int((total-listado)//0.05)
listado = listado + cincocent*0.05

umcent = (total-listado)*100

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%cem)
print("%d nota(s) de R$ 50.00"%cinquenta)
print("%d nota(s) de R$ 20.00"%vinte)
print("%d nota(s) de R$ 10.00"%dez)
print("%d nota(s) de R$ 5.00"%cinco)
print("%d nota(s) de R$ 2.00"%dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%um)
print("%d moeda(s) de R$ 0.50"%cinqcent)
print("%d moeda(s) de R$ 0.25"%vintcinco)
print("%d moeda(s) de R$ 0.10"%dezcent)
print("%d moeda(s) de R$ 0.05"%cincocent)
print("%.0f moeda(s) de R$ 0.01"%umcent)

