n = int(input())

for i in range(1, n+1):
    if i%2 == 0:
        quadrado = i*i
        print("%d^2 = %d"%(i,quadrado))