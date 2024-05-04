def leerFichero(rutaFichero):
    try:
        with open(rutaFichero, 'r') as f:
            contenido = f.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo no se encontró en la ruta {rutaFichero}.")
leerFichero("100 ejercicios python/100_ejercicios_python/prueba.txt")