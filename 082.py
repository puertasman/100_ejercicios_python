import math

def esPrimo(numero):
    for i in range (2,math.ceil(math.sqrt(numero))):
        if numero % i == 0:
            return False
    return True

def esCirculoPrimo(numero):
    numero_cadena = str(numero)
    for i in range (len(numero_cadena)):
        num = int(numero_cadena[i:]+numero_cadena[:i])
        if not esPrimo(num):
            return False
    return True
    
print(esCirculoPrimo(3))
print(esCirculoPrimo(81))
print(esCirculoPrimo(191))
print(esCirculoPrimo(9377))
print(esCirculoPrimo(36))
