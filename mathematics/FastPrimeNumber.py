n = int(input(""))

numeros = []
outputs = []
for x in range(n):
  num = int(input(""))
  numeros.append(num)

for x in range(n):

  if numeros[x] % 2 == 0 or numeros[x] % 3 == 0 or numeros[x] % 5 == 0 or numeros[x] % 7 == 0:
      print("Not Prime")
  else:
    print("Prime")