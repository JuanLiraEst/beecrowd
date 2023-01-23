from math import factorial
while True:
    try:
        l = input()
        v = l.split(" ")

        a = int(v[0])
        b = int(v[1])

        dif = abs(a-b)
        print(dif)

        

    except EOFError:
        break       
