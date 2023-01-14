x = int(input())
y = int(input())
maior = 0
menor = 0
if y>=x:
    maior = y
    menor = x

else:
    maior = x
    menor = y

sum = 0

for i in range(menor+1,maior):
    if i%2!=0:
        sum = sum + i

print(sum)