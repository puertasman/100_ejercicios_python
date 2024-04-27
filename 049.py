def numValoresDicc(d):
    elementos = 0
    for i in d.keys():
        elementos += len(d[i])
    return elementos

print(numValoresDicc({"a": [1,2,3], "b": [3,'p'], "c": [8]}))

print(numValoresDicc({"Julie": [12,60.1], "Fred": [26,75.6], "David": []}))