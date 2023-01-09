from math import sqrt
x1y1 = input()
x2y2 = input()

v1 = x1y1.split(" ")
v2 = x2y2.split(" ")

x1 = float(v1[0])
y1 = float(v1[1])
x2 = float(v2[0])
y2 = float(v2[1])

dist = float(sqrt( ((x2-x1)**2)+((y2-y1)**2)  ))

print("%.4f"%dist)


