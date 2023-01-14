i = 1
j = 7
counter = 0
while True:
    print("I=%d J=%d"%(i,j))
    j-=1
    counter+=1
    if counter == 3:
        counter = 0
        j = j+5
        i+=2
    if i == 11:
        break