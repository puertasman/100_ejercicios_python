def leerFichero(rutaFichero):
    with open(rutaFichero, 'r') as f:
        contenido = f.read()
        print(contenido)
    
leerFichero("prueba.txt")