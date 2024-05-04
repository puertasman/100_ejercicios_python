def eliminarCaracter(rutaFichero, caracter):
    with open(rutaFichero, 'r', encoding='utf-8') as f:
        texto = f.read()
        texto = texto.replace(caracter, "")
    
    with open("100 ejercicios python/100_ejercicios_python/prueba_modificado.txt", "w+", encoding = 'utf-8') as f:
        f.write(texto)
    
print(eliminarCaracter("100 ejercicios python/100_ejercicios_python/prueba.txt","a"))