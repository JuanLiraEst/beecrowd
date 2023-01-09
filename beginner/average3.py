valores = input()

v = valores.split(" ")

n1 = float(v[0])
n2 = float(v[1])
n3 = float(v[2])
n4 = float(v[3])

media = (n1*2 + n2*3 + n3*4 + n4)/10

print("Media: %.1f"%media)

if media>=7:
    print("Aluno aprovado.")

elif media<5:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame: %.1f"%n5)
    mediaf = (n5 + media)/2
    
    if mediaf>=5:
        print("Aluno aprovado.")
        print("Media final: %.1f"%mediaf)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f"%mediaf) 