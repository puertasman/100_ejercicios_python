def sumar_numeros(numero):
    lista_numeros = [int(i) for i in str(numero)]
    return sum(lista_numeros) 

def codigoSuma(numero):
    if numero > 100:
        nuevo_numero = sumar_numeros(numero)
        while nuevo_numero > 9:
            nuevo_numero = sumar_numeros(nuevo_numero)
        return int(str(nuevo_numero) + str(numero))
    else:
        return "Número no válido"
    

print(codigoSuma(69810))

print(codigoSuma(3201))

print(codigoSuma(55))