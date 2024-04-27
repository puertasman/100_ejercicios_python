def minimo(L):
    min = L[0]
    for i in range(1,len(L)):
        if L[i] < min:
            min = L[i]
    return(min)

print(minimo([-9,2,4,1,8]))

print(minimo([-3,1,7,6,2,3]))