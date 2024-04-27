def divisor(n):
    divisores = []
    for i in range(1,n+1):
        if n % i == 0:
            divisores.append(i)
    return divisores

print(divisor(3))
print(divisor(9))