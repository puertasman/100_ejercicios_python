import re

def numOcFichero(rutaFichero, palabra):
    with open(rutaFichero, "r") as f:
        contenido = f.read()
        contenido =  re.sub(r'[^\w\s]', '', contenido)
        contenido = contenido.split()
        return(contenido.count(palabra))
    
    
# sin re
def numOcFichero_sinre(rutaFichero, palabra):
    with open(rutaFichero, "r", encoding ='utf-8') as f:
        contenido = f.read()
        contenido =  contenido.replace('\n', ' ')
        print(contenido)
        contenido = contenido.split(' ')
        return(contenido.count(palabra))


    
print(numOcFichero("100 ejercicios python/100_ejercicios_python/prueba.txt","a"))
print(numOcFichero_sinre("100 ejercicios python/100_ejercicios_python/prueba.txt","a"))