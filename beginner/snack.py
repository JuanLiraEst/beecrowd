l = input()

v = l.split(" ")

x = int(v[0])
y = int(v[1])

cash = [4.0 , 4.5 , 5.0 , 2.0, 1.5]

total = cash[x-1]*y

print("Total: R$ %.2f"%total)
