def reemplazar(frase,palabra,nuevaPalabra):
    palabras = frase.split()
    for i,pal in enumerate(palabras):
        if pal == palabra:
            palabras[i] = nuevaPalabra
    return " ".join(palabras)

print(reemplazar("Hola Aurélie", "Aurélie", "Mathilde"))

print(reemplazar("Tengo 50 años","50","35"))