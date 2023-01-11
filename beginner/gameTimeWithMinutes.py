entrada = input()

v = entrada.split(" ")

a = int(v[0])
b = int(v[1])
c = int(v[2])
d = int(v[3])

end = c*60 + d
start = a*60 + b
minutagem = 0
horas = 0
min = 0

#se as horas forem iguais
if a == c and b == d:
    horas = 24
    min = 0

#se a hora do final for maior
if end>start:
    minutagem = end-start
    horas = minutagem//60
    min = minutagem%60

#se a hora do final for menor
if start>end:
    #24h menos a diferença
    minutagem = 1440 - (start-end) 
    horas = minutagem//60
    min = minutagem%60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(horas,min))