def esDistinto(numero):
    numeros = str(abs(numero))
    return len(numeros) == len(set(numeros))

print(esDistinto(9647))
print(esDistinto(1343))