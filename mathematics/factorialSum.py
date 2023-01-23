from math import factorial
while True:
    try:
        l = input()
        v = l.split(" ")

        m = int(v[0])
        n = int(v[1])

        sum = factorial(m) + factorial(n)

        print(sum)

    except EOFError:
        break       

