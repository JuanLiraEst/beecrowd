l = input()

v = l.split(" ")

a = int(v[0])
b = int(v[1])

hora = 0
if a == b:
    hora = 24

elif b>a:
    hora = b-a

else:
    hora = 24-a + b

print("O JOGO DUROU %d HORA(S)"%hora)