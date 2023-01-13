n = int(input())

h = n//3600
min = (n%3600)//60
s = n%3600%60

print("%d:%d:%d"%(h,min,s))