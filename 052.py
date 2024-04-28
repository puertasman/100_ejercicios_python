def divisoresMult(n,a,numUmbral):
    lista = []
    for i in range(numUmbral):
        if i % n == 0 and i % a != 0:
            lista.append(i)
    return lista

print(divisoresMult(5,2,100))
print(divisoresMult(11,3,85))