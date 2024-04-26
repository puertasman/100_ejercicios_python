def sumarDigitos(num):
    suma = 0
    for i in str(num):
        suma += int(i)
    return suma

print(sumarDigitos(149))
print(sumarDigitos(3018))