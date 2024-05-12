class ListaPerso:
    def __init__(self,*numeros):
        self.numeros = []
        for numero in numeros:
            if type(numero) == int or type(numero) == float:
                self.numeros.append(numero)
            else:
                print(f"Operación no permitida: no es posible agregar el tipo {type(numero)} a la lista")
    
    def append(self,elemento):
        if type(elemento) == int or type(elemento) == float:
            if elemento in self.numeros:
                print(f"El número {elemento} ya se encuentra en la lista, no se puede añadir.")
            else:
                self.numeros.append(elemento)
                print(f"Número {elemento} añadido a la lista.")
        else:
            print(f"Operación no permitida: no es posible agregar el tipo {type(elemento)} a la lista")
            
    def __str__(self):
        return(str(self.numeros))
L1 = ListaPerso(5,2,3,7,9, "a")
print(L1)

L1.append(2)

L1.append("abc")

L1.append(10)
print(L1)

L1.append([3,2,2])