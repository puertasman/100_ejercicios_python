def longitud(L):
    tamanyo = 0
    for i in L:
        tamanyo += 1
    return tamanyo

print(longitud([3,6,7,"abde",[1,3,57],True]))

print(longitud([]))