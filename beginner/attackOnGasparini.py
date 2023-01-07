#STILL WRONG ANSWER USING PYTHON
linha1 = input()
linha2 = str(input()) 
linha3 = input()

v1 = linha1.split(" ")
n = int(v1[0])
muro = int(v1[1])
x = int(v1[1])

v2 = list(linha2)
p = 0
m = 0
g = 0

#pegar a qtde de titans
for i in range(n):
  if v2[i] == "P":
    p+=1
  elif v2[i] == "M":
    m+=1
  elif v2[i] == "G":
    g+=1

v3 = linha3.split(" ")
h_p = int(v3[0])
h_m = int(v3[1])
h_g = int(v3[2])

h_titans = int(p*h_p + m*h_m + g*h_g)

while x< h_titans:
  x = x + muro


qtd_muros = int(x/muro)
print(qtd_muros)