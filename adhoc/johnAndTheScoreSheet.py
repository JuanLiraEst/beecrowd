n = int(input())

for x in range(n):
    time = input()
    v = time.split(" ")

    min = int(v[0])
    tempo = v[1]

    if tempo == "1T":
        if min>45:
            resto = min-45
            print("45+%d"%resto)
        else:
            print(min)
    
    elif tempo == "2T":
        if min>45:
            resto = min-45
            print("90+%d"%resto)

        else:
            print(45+min)


