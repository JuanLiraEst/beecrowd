salario = float(input())

if salario<=2000:
    print("Isento")

elif 2000<salario<=3000:
    taxa = (salario- 2000)*(8/100)
    print("R$ %.2f"%taxa)

elif 3000<salario<=4500:
    taxa = 80 + ((salario - 3000)*(18/100))
    print("R$ %.2f"%taxa)

else:
    taxa = 80 + 270 + ((salario - 4500)*(28/100))
    print("R$ %.2f"%taxa)
