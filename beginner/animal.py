l1 = input()
l2 = input()
l3 = input()

a = ["ave", "carnivoro", "aguia"]
b = ["ave", "onivoro", "pomba"]
c = ["mamifero", "onivoro", "homem"]
d = ["mamifero", "herbivoro", "vaca"]
e = ["inseto", "hematofago", "pulga"]
f = ["inseto", "herbivoro", "lagarta"]
g = ["anelideo", "hematofago", "sanguessuga"]
h = ["anelideo", "onivoro", "minhoca"]

table = [a,b,c,d,e,f,g,h]

for i in range(8):
    if table[i][0] == l2 and table[i][1] == l3:
        print(table[i][2])