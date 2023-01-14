n = int(input())
outputs = []
for x in range(n):
    i = int(input())
    if i == 0:
        outputs.append("NULL")
    elif i<0:
        if i%2 ==0:
            outputs.append("EVEN NEGATIVE")
        else:
            outputs.append("ODD NEGATIVE")
    
    elif i>0:
        if i%2 ==0:
            outputs.append("EVEN POSITIVE")
        else:
            outputs.append("ODD POSITIVE")

for y in range(n):
    print(outputs[y])
