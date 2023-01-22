gremio = 0
inter = 0
empate = 0
grenais = 0
def placar(inter,gremio,empate,grenais):
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

def resultados():
    print("%d grenais"%grenais)
    print("Inter:%d"%inter)
    print("Gremio:%d"%gremio)
    


def main():
    while True:
        placar(inter,gremio,empate,grenais)
        print("Novo grenal (1-sim 2-nao)")
        resp = int(input())
        if resp == 1:
            placar(inter,gremio,empate,grenais)

        elif resp == 2:
            resultados()
            break

main()