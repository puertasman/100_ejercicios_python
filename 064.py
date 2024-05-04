def presenciaNumero(rutaFichero):
    with open(rutaFichero, "r", encoding='utf-8') as f:
        texto = f.read()
        for letra in texto:
            if letra.isdigit():
                return True
        return False
    
print(presenciaNumero("100 ejercicios python/100_ejercicios_python/prueba.txt"))