l1 = input()
l2 = input()

v1 = l1.split(" ")
v2 = l2.split(" ")

qtd1 = int(v1[1])
qtd2 = int(v2[1])

val1 = float(v1[2])
val2 = float(v2[2])

pgto = float(qtd1*val1 + qtd2*val2)

print("VALOR A PAGAR: R$ %.2f"%pgto)