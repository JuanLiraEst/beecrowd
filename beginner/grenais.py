gremio = 0
inter = 0
empate = 0
grenais = 0

while True:
    l = input()
    v = l.split(" ")
    i = v[0] #inter
    g = v[1] #gremio

    if i>g:
        inter+=1
    elif g>i:
        gremio+=1
    else:
        empate+=1
    grenais+=1

    print("Novo grenal (1-sim 2-nao)")
    resp = int(input())
    if resp == 1:
        continue

    elif resp == 2:
        print("%d grenais"%grenais)
        print("Inter:%d"%inter)
        print("Gremio:%d"%gremio)
        print("Empates:%d"%empate)
        
        if inter>gremio:
            print("Inter venceu mais")
        if gremio>inter:
            print("Gremio venceu mais")
        break
