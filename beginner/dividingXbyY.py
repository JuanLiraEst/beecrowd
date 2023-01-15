n = int(input())
resultado = 0.0
for i in range(n):
    l = input()
    v = l.split(" ")
    x = int(v[0])
    y = int(v[1])
    
    if y == 0:
        print("divisao impossivel")
    else:
        resultado = x/y
        print("%.1f"%resultado)
