pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range (5):
    n = float(input())
    if n%2==0:
        pares+= 1
    if n%2!=0:
        impares+=1
    if n>0:
        positivos+=1
    if n<0:
        negativos+=1

print("%d valor(es) par(es)"%pares)
print("%d valor(es) impar(es)"%impares)
print("%d valor(es) positivo(s)"%positivos)
print("%d valor(es) negativo(s)"%negativos)