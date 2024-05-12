import os

def tratamientoFichero(rutaFichero):
    with open(rutaFichero, "r") as f:
        texto = f.read()
        texto = texto.replace("\n"," ")
    nueva_ruta, extension = os.path.splitext(rutaFichero)
    nueva_ruta = nueva_ruta + '_sin_saltos' + extension
    with open(nueva_ruta, "w+") as f:
        f.write(texto)
        
tratamientoFichero("100 ejercicios python/100_ejercicios_python/fichero_con_saltos_linea.txt")
tratamientoFichero("100 ejercicios python/100_ejercicios_python/prueba.txt")