def calculoFactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(calculoFactorial(3))
print(calculoFactorial(9))
print(calculoFactorial(0))
