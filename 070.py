import random
import string


lista_caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generarContrasena(caracteres,longitud):
    random.shuffle(lista_caracteres)
    contrasena = ""
    for i in range (longitud):
        contrasena += str(random.choice(caracteres))
    return contrasena

print(generarContrasena(lista_caracteres,10))


# en todos sitios se podría hacer shuffles para que quedaran más mezclados 
# además se podría hacer con una lista para mezclarlos aún más y luego un join
        