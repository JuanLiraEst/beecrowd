entrada = input()

v = entrada.split(" ")

a = int(v[0])
b = int(v[1])
c = int(v[2])

maiorAB = (a+b+abs(a-b))/2

a = maiorAB
b = c

maiorAB = (a+b+abs(a-b))/2

print("%d eh o maior"%maiorAB)