i = 1
j = 7

while True:
    print("I=%d J=%d"%(i,j))
    j-=1
    if j == 4:
        j = 7
        i+=2
    if i == 11:
        break