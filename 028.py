import time
tiempo_inicio = time.time()

#programa
for i in range(11):
    print(f"8 x {i} = {i*8}")

tiempo_fin = time.time()
print(f"El programa ha tardado {tiempo_fin-tiempo_inicio}")