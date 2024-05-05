def claveMaxValDicc(d):
    indices = -1
    posicion = ''
    for i in d:
        elementos = len(set(d[i]))
        if elementos > indices:
            posicion = i
            indices = elementos
    return posicion

print(claveMaxValDicc({"a": [9,10,9,7,3,1], "b": [5,3,2,2,2], "c": [1,1,1,1,1,1,8,2]}))
print(claveMaxValDicc({"dtg":[6,8,1],"fgb":[2.5,"a"],"klm":["p",3,3]}))