cords = input()

xy = cords.split(" ")

x = float(xy[0])
y = float(xy[1])

if x == 0 and y == 0:
    print("Origem")

if x == 0 and y!=0:
    print("Eixo Y")

if y == 0 and x!=0:
    print("Eixo X")

if x>0 and y>0:
    print("Q1")

if x>0 and y<0:
    print("Q4")

if x<0 and y<0:
    print("Q3")

if x<0 and y>0:
    print("Q2")