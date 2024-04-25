L = []
L.extend([10, 25, 30, 45, 90,'ab','cd','ef'])
print(L)

# También se podría hacer con una suma
L = []
L += [10, 25, 30, 45, 90,'ab','cd','ef']
print(L)

# O recorriendo y añadiendo
L = []
elementos = [10, 25, 30, 45, 90,'ab','cd','ef']
for e in elementos:
    L.append(e)
print(L)