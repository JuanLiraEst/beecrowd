n = int(input())
dentro = 0
for x in range(n):
    i = int(input())
    if 10<=i<=20:
        dentro+=1

fora = n-dentro
print("%d in\n%d out"%(dentro,fora))
