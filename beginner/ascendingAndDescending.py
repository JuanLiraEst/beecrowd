outputs = []
while True:
    l = input()
    v = l.split(" ")
    x = int(v[0])
    y = int(v[1])

    if x>y:
        outputs.append("Decrescente")
    elif y>x:
        outputs.append("Crescente")

    else:
        break

for x in range(len(outputs)):
    print(outputs[x])
