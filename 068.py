lista_usuario = []
num_elementos = -1
while num_elementos < 0:
    try:
        num_elementos = int(input("Introduce el número de elementos que va a tener la lista: "))
    except:
        print("El número introducido no es válido.")
        
if num_elementos == 0:
    print("No hay nada para mostrar")
else:
    for i in range (num_elementos):
        while len(lista_usuario) < i+1:
            try:
                valor = int(input("Introduce un número entero: "))
                lista_usuario.append(valor)
            except:
                print("El valor debe ser entero.")
                
print(lista_usuario)