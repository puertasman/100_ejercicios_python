def secuenciaFibonacci(N):
    if N <= 2:
        return 1
    else:
        return secuenciaFibonacci(N-1) + secuenciaFibonacci(N-2)
        
        
print(secuenciaFibonacci(25))

print(secuenciaFibonacci(35))