import os
def nombreFichero(rutaDirectorio):
    contenido = os.listdir(rutaDirectorio)
    print(contenido)
    
    return sum(os.path.isfile(os.path.join(rutaDirectorio, elemento)) for elemento in contenido)
    
print(nombreFichero("100 ejercicios python/100_ejercicios_python/"))
print(nombreFichero("100 ejercicios python/"))
print(nombreFichero(os.path.dirname(os.path.abspath(__file__))))  # ubicacion del fichero actual