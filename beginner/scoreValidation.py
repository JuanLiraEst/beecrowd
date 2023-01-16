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

