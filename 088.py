def ordenamientoAsc(L):
    n = len(L)
    # Se repite el proceso n-1 veces
    for i in range(n):
        # Iniciamos un indicador de intercambio
        intercambio = False
        # Comparamos elementos adyacentes
        for j in range(0, n-i-1):  # Se reduce el rango porque el último elemento de cada pasada ya está en su lugar
            if L[j] > L[j + 1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                L[j], L[j + 1] = L[j + 1], L[j]
                intercambio = True
        # Si no se hizo ningún intercambio, la L ya está ordenada
        if not intercambio:
            break
    return L
    
print(ordenamientoAsc([6,1,9,-6,1,8,7]))

print(ordenamientoAsc([-3,5.3,2,7,1,2.3,9.5]))