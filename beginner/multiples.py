entrada = input()

v = entrada.split(" ")

a = int(v[0])
b = int(v[1])

if b>a:
    b = int(v[0])
    a = int(v[1])

if a%b==0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")