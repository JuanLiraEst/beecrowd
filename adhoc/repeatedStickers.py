n = int(input())
figs = []
novas = 0
repetidas = 0

for x in range(n):
    fig = int(input())
    if fig not in figs:
        novas += 1
        figs.append(fig)
    else:
        repetidas += 1

print(novas)
print(repetidas)
