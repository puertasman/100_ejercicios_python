def esUnPalindromo(numero):
    if numero < 10:
        return False
    cadena = str(numero)
    inversa = int(cadena[::-1])
    return numero == inversa

print(esUnPalindromo(10))

print(esUnPalindromo(919))

print(esUnPalindromo(16843))

print(esUnPalindromo(4231324))