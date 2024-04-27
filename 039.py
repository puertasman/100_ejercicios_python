def anadirElementoDicc(clave,valor,d):
    d[clave] = valor

dicc =  {'julien': 14, 'laurent': 31}
anadirElementoDicc('baptiste', 29, dicc)
print(dicc)

dicc = {}
anadirElementoDicc('peso',65.3,dicc)
print(dicc)
