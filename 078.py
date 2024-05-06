def split(frase,caracter):
    lista = []
    palabra_tmp = ""
    if caracter in frase:
        for i in range(len(frase)):
            if frase[i] != caracter:
                palabra_tmp += frase[i]
                if i == len(frase)-1:
                    lista += [palabra_tmp]
                    return lista
            else:
                lista += [palabra_tmp]
                palabra_tmp = ""            
        
    else:
        lista = [frase]
        return lista
        
    
print(split("Hola Aurélie"," "))

print(split("Hola Aurélie, qué tal"," "))

print(split("Hola.¿Está bien?","."))