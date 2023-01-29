i = input()
v = i.split(" ")

n = int(v[0])
l = int(v[1])
ml = int(v[2])

qtd = float(n*ml/1000)

x = 0
while True:
    x+=1
    if x>=qtd and x%l==0:
        print(x)
        break

