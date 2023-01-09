valores = input()

v = valores.split(" ")

v.sort() #ordenando
v1 = float(v[0])
v2 = float(v[1])
v3 = float(v[2])

triang = []
triang.append(v1)
triang.append(v2)
triang.append(v3)
triang.sort()

c = triang[0]
b = triang[1]
a = triang[2]

if a>= b + c:
    print("NAO FORMA TRIANGULO")

elif a*a == b*b + c*c:
    print("TRIANGULO RETANGULO")

elif a*a > b*b + c*c:
    print("TRIANGULO OBTUSANGULO")

elif a*a < b*b + c*c:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")

if a == b != c or b == c != a or a == c != b:
    print("TRIANGULO ISOSCELES") 