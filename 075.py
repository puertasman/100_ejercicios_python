def numeroPar(N):
    if N == 1:
        return False
    return numeroImpar(N-1)

def numeroImpar(N):
    if N == 1:
        return True
    return numeroPar(N-1)

print(numeroPar(5))

print(numeroImpar(7))