l = input()
v = l.split(" ")
a = int(v[0])
b = int(v[1])
soma = 0
for x in range(a, b+1):
    soma = soma+x
print(soma)
