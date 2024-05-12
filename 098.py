def ordenarDicc(d):
    indices = d.keys()
    indices = list(indices)
    indices.sort()
    dict = {}
    for i in indices:
        dict[i] = d[i]
    return dict

print(ordenarDicc({"c":3,"a":9,"e":1}))

print(ordenarDicc({8: 9, 2: 3, 9: 11}))
