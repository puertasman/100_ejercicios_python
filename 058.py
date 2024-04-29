def numeroOcurrencias(L):
    apariciones = {}
    for numero in L:
        if numero not in apariciones:
            apariciones[numero] = 1
        else:
            apariciones[numero] += 1
    apariciones = [(aparicion, apariciones[aparicion]) for aparicion in apariciones]
    return apariciones

print(numeroOcurrencias([-4,8,-3,2,1,2,7,9,-3,8,1]))

print(numeroOcurrencias(["a",3,4,"b","a",3]))
