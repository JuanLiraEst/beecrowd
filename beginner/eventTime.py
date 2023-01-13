l1 = input()
l2 = input()
l3 = input()
l4 = input()

#split divide a string em 2 partes
#estou pegando a parte do num
dia1 = int(l1.split(" ")[1])
dia2 = int(l3.split(" ")[1])

horario1 = l2.split(" : ")
horario2 = l4.split(" : ")

h1 = int(horario1[0])
m1 = int(horario1[1])
s1 = int(horario1[2])

h2 = int(horario2[0])
m2 = int(horario2[1])
s2 = int(horario2[2])

#passando tudo pra segundos
start = dia1*86400 + h1*3600 + m1*60 + s1
end = dia2*86400 + h2*3600 + m2*60 + s2

total = end-start

days = total//86400
hours = (total%86400)//3600
minutes = (total%86400%3600)//60
seconds = total%86400%3600%60

print("%d dia(s)"%days)
print("%d hora(s)"%hours)
print("%d minuto(s)"%minutes)
print("%d segundo(s)"%seconds)

