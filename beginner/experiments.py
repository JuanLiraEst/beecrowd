n = int(input())

c = 0
r = 0
s = 0

for x in range(n):
    teste = input()
    v = teste.split(" ")
    qtd = int(v[0])

    if v[1] == "C":
        c = c + qtd
    if v[1] == "R":
        r = r + qtd
    if v[1] == "S":
        s = s + qtd

total = c+r+s
perc_c = float((c*100)/total)
perc_r = float((r*100)/total)
perc_s = float((s*100)/total)

print("Total: %d cobaias"%total)
print("Total de coelhos:",c)
print("Total de ratos:",r)
print("Total de sapos:",s)
print("Percentual de coelhos: %.2f"%perc_c,"%")
print("Percentual de ratos: %.2f"%perc_r,"%")
print("Percentual de sapos: %.2f"%perc_s,"%")
