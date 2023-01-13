ddd = [61,71,11,21,32,19,27,31]

dest = ["Brasilia","Salvador","Sao Paulo",
        "Rio de Janeiro", "Juiz de Fora", 
        "Campinas", "Vitoria", "Belo Horizonte"]

n = int(input())
c = 0
for x in range(8):
    if ddd[x] == n:
        print(dest[x])
        c+=1

if c == 0:
    print("DDD nao cadastrado")
