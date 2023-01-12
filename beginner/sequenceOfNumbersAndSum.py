ms = []
ns = []

while True:
    valores = input()
    v = valores.split(" ")
    m = int(v[0])
    n = int(v[1])

    if m <= 0 or n <= 0 or (m <= 0 and n <= 0) :
        break
    else:
        if m<=n:
            ms.append(m)
            ns.append(n)
        else:
            ms.append(n)
            ns.append(m)

for x in range(len(ms)):
    m = ms[x]
    n = ns[x]
    soma = 0
    for y in range(m-1,n):
        print(y+1, end = " ")
        soma = soma + (y+1)
    print("Sum=%d"%soma)