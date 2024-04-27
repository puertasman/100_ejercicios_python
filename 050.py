def concatDicc(d1, d2):
    d1.update(d2)
    return d1


print(concatDicc({"a": 3, "b": 6}, {"c": 2, "d": -1}))

print(concatDicc({"d": [2.9, 4.1]}, {"p": []}))
