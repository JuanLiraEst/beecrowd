def calculaMedia():
    x = 0
    media = 0
    while x < 2:
        value = float(input())

        if value<0 or value>10:
            print("nota invalida")
            x = x
        
        else:
            media = media + value
            x+=1

    media = media/2

    print("media = %.2f"%media)

def reinicia():
    while True:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())
        if novo == 1:
            calculaMedia()

        elif novo == 2:
            break


def main():
    calculaMedia()
    reinicia()

main()