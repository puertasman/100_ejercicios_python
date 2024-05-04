def escribirFichero(rutaFichero, texto):
    with open(rutaFichero, "w+", encoding = 'utf-8') as f:
        f.write(texto)
   
print(escribirFichero("100 ejercicios python/100_ejercicios_python/new_one.txt","Pon esto en el fichero"))