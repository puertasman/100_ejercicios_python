def mediaLista(L):
    suma = 0
    tam = 0
    for i in L:
        suma += i
        tam += 1
    return suma/tam


print(mediaLista([1, 2, 3, 4, 5, 6, 7]))

print(mediaLista([3, 0, -1, 5, 6, 9, 17]))