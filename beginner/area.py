pi = 3.14159

valores = input()

v = valores.split(" ")

a = float(v[0])
b = float(v[1])
c = float(v[2])

tri = (a*c)/2
circ = pi*(c**2)
trap = ((a+b)*c)/2
quad = b**2
ret = a*b

print("TRIANGULO: %.3f"%tri)
print("CIRCULO: %.3f"%circ)
print("TRAPEZIO: %.3f"%trap)
print("QUADRADO: %.3f"%quad)
print("RETANGULO: %.3f"%ret)