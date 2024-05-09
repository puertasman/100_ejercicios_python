def busquedaDicotomica(L, elt):
    L.sort()
    inicio = 0
    fin = len(L)-1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = L[medio]
        if valor_medio == elt:
            return True
        elif valor_medio < elt:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False
    
    
print(busquedaDicotomica([6,9,15,36,41,43,47],41))

print(busquedaDicotomica([-9,-1,3,4,7,11],0))