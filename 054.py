def EliminarEsp(frase):
    return frase.replace(" ", "")

print(EliminarEsp("Francia es hermosa."))

print(EliminarEsp("Me llevaré mi bicicleta"))

def EliminarEspV2(frase):
    frase = frase.split(" ")
    frase = "".join(frase)
    return frase.replace(" ", "")

print(EliminarEspV2("Francia es hermosa."))

print(EliminarEspV2("Me llevaré mi bicicleta"))

