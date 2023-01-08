age = int(input())

anos = age//365

resto = age-365*anos

meses = resto//30

dias = age-365*anos-30*meses

print("%d ano(s)"%anos)
print("%d mes(es)"%meses)
print("%d dia(s)"%dias)