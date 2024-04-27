def ControlMay(frase):
    for i in frase:
        if i.isupper():
            return True
    return False

print(ControlMay("Las verduras son buenas para la salud"))

print(ControlMay("estoy aprendiendo el lenguaje python"))