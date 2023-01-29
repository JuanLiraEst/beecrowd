quadrantes = []
while True:
    cords = input()

    xy = cords.split(" ")

    x = float(xy[0])
    y = float(xy[1])

    if x == 0 and y == 0:
        break

    if x == 0 and y!=0:
        break

    if y == 0 and x!=0:
        break

    if x>0 and y>0:
        quadrantes.append("primeiro")

    if x>0 and y<0:
        quadrantes.append("quarto")

    if x<0 and y<0:
        quadrantes.append("terceiro")

    if x<0 and y>0:
        quadrantes.append("segundo")

for z in range(len(quadrantes)):
    print(quadrantes[z])
