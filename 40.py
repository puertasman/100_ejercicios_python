def maximo(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max

print(maximo([-9,2,4,1,8]))

print(maximo([-3,1,7,6,2,3]))