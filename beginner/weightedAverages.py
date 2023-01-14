n = int(input())
averages = []

for x in range(n):
    values = input()
    v = values.split(" ")
    a = float(v[0])
    b = float(v[1])
    c = float(v[2])
    med = (a*2 + b*3 + c*5)/10
    averages.append(med)

for x in range(n):
    print("%.1f"%averages[x])
