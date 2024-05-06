L = []

for i in range(100,1000):
    centenas = i // 100
    decenas = i % 100 // 10
    unidades = i % 10
    if (centenas * decenas * unidades) % (centenas + decenas + unidades) == 0:
        if (centenas * decenas * unidades) != 0:
            L.append(i)

print(L)