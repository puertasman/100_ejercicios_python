def sumaMayor(L):
    total = 0
    for i in range(len(L)):
        total += sum(L[i:])
    return total

print(sumaMayor([-8,-4,6,8,-6,10,-4,-4]))

print(sumaMayor([-6,1,8,-7,1,9,-1,2]))ijuiujhguiiguhouñouñhl