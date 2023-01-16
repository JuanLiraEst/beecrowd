l = input()
v = l.split(" ")

x = int(v[0])
y = int(v[1])
c = 0
for i in range(y):
    n = i+1
    if c == x-1:
        print(n, end = "")
    elif c == x:
        c = 0
        print("\n%d"%n, end = " ")

    else:
        print(n, end = " ")
    c+=1


