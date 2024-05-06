def calcularSuma(L):
    suma = 0
    if len(L) == 0:
        return 0
    return L[0] + calcularSuma(L[1:])
    
print(calcularSuma([3,2,6,9,-1,5]))
print(calcularSuma([-3,-6,0,1,2,7]))