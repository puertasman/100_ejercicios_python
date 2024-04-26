def eliminarDuplicados(L):
    l = list(set(L))
    l.sort()
    return l

print(eliminarDuplicados([0,3,5,7,3,5,1,-1]))
print(eliminarDuplicados([0,5,9,10,3,2,1,-3]))