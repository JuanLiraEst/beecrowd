mes = int(input())

meses_n = [1,2,3,4,5,6,7,8,9,10,11,12]


months = ["January", "February", "March", "April",
 "May", "June", "July", "August", 
"September", "October", "November", "December" ]

for x in range(12):
    if meses_n[x] == mes:
        print(months[x])