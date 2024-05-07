def isdigit(cadena):
    digit = '1234567890'
    for i in cadena:
        if i not in digit:
            return False
    return True

print(isdigit("125920"))

print(isdigit("edgte9be"))