def presenciaVocal(frase):
    for letra in frase:
        if letra in "aeiou":
            return True
    return False

print(presenciaVocal("Voy a darme una ducha"))
print(presenciaVocal("rbhpm"))