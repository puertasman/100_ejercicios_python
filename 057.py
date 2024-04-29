def invertirFrase(frase):
    frase_cortada = frase.split(" ")
    frase_invertida = frase_cortada[::-1]
    frase = " ".join(frase_invertida)
    return frase

print(invertirFrase("Hola a todo el mundo"))
print(invertirFrase("Manzana"))