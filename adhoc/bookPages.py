p = int(input())
pages = 0
for x in range(1,p+1):
    digito = str(x)
    
    pages = pages + len(digito)

print(pages)