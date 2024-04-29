def unionLista(L1,L2,L3):
    lista_entera = L1 + L2 + L3
    lista_sin_duplicados = set(lista_entera)
    lista_entera = list(lista_sin_duplicados)
    lista_entera.sort()
    return lista_entera

print(unionLista([3,6,9,3],[1,0,3],[12,6,0]))

print(unionLista([7,44,-3],[],[7,2,7]))