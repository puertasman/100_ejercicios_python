def filtrarPalabras(frase,longitudMinima):
    palabras = frase.split()
    frase_filtrada = []
    for palabra in palabras:
        if len(palabra) >= longitudMinima:
            frase_filtrada.append(palabra)
    return " ".join(frase_filtrada)

print(filtrarPalabras("Hola a todos",4))

print(filtrarPalabras("¿Cuál es tu origen?",3))