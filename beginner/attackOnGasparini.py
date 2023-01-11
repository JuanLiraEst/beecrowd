linha1 = input()
linha2 = str(input()) 
linha3 = input()

v1 = linha1.split(" ")
v2 = list(linha2)
v3 = linha3.split(" ")

titans = int(v1[0])
h_muro = int(v1[1])
h_p = int(v3[0])
h_m = int(v3[1])
h_g = int(v3[2])

fila = []
muros = [h_muro]

#botando as alturas em ordem numa lista
for i in range(titans):
  if v2[i] == "P":
    fila.append(h_p)

  elif v2[i] == "M":
    fila.append(h_m)

  elif v2[i] == "G":
    fila.append(h_g)

i = 0
m = 0
#batendo eles no muro
while i < titans:
  
  if muros[m] >= fila[i]:
    muros[m] = muros[m] - fila[i]
    fila[i] = 0
    i+=1
    m = 0

  elif muros[m]<fila[i] and m+1 == len(muros):
    muros.append(h_muro)
    m+=1
  elif muros[m]< fila[i]:
    m+=1

print(len(muros))
