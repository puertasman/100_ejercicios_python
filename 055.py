def posicionEltLista(L,x):
    posicion = []
    for i in range(len(L)):
        if L[i] == x:
            posicion.append(i)
    if len(posicion) == 0:
        posicion = f"El elemento {x} no se encuentra en la lista {L}"
    return posicion

print(posicionEltLista([1,2,3,6,8,7,3],3))

print(posicionEltLista([6,8,9,1,3,7],-1))

