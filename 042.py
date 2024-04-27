for i in range(1,7):
    if i < 3:
        print(i*"*")
    else:
        print(2*(i-1)*"*")

# otra solución

print("\n================================")
print("esta segunda es algo más óptima")
for i in range (1,11):
    if i == 1 or i % 2 == 0:
        print(i*"*")