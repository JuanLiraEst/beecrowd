'''
#Faltou conseguir passar os floats que terminam em .0 pra int
#mas a sequencia sai certo
def print_i():
    if i.is_integer() == True:
        print("I=%d"%i, end= " ")
    else:
        print("I=%.1f"%i, end= " ")

def print_j():
    if j.is_integer() == True:
        print("J=%d"%j)
    else:
        print("J=%.1f"%j)
i = 0.0
j = 1.0
c = 0
while True:

    print_i()
    print_j()

    c+=1
    j = j + 1

    if c == 3: 
        c = 0
        j = j - 2.8
        i = i + 0.2



    if i>4:
        break
'''
i = [0 , 0 , 0 , 0.2 , 0.2 , 0.2 , 0.4 , 0.4 , 0.4 ,
0.6 , 0.6 , 0.6 , 0.8 , 0.8 , 0.8 , 1 , 1 , 1, 1.2 , 
1.2 , 1.2 , 1.4 , 1.4 , 1.4 , 1.6 , 1.6 , 1.6 , 1.8 ,
1.8 , 1.8 , 2 , 2 , 2]

j = [1 , 2 , 3 , 1.2 , 2.2 , 3.2 ,1.4 , 2.4 , 3.4 ,
1.6 , 2.6 , 3.6 ,1.8 , 2.8 , 3.8 ,2 , 3 , 4 ,
2.2 , 3.2 , 4.2 ,2.4 , 3.4 , 4.4 , 2.6 , 3.6 , 4.6 ,
2.8 , 3.8 , 4.8 ,3 , 4, 5 ]

for x in range(33):
    if x<3 or 14<x<18 or x>29:
        print("I=%d J=%d"%(i[x],j[x]))
    else:
        print("I=%.1f J=%.1f"%(i[x],j[x]))