x = int(input())
lista = []
for y in range(10):
    lista.append(x)
    x=x*2

for z in range(20):
    print("N[%d] = %d"%(z,lista[z]))
