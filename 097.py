import string
numeros = list(string.digits) + [",", "."]

class CadenaPerso:
    def __init__(self,cadena):
        for letra in cadena:
            if letra in numeros:
                print("La instancia sólo debe contender letras alfabéticas.")
                print(f"El carácter '{letra}' será eliminado.")
                cadena = cadena.replace(letra,"")
        self.cadena = cadena

    def __add__(self,nueva_cadena):
        if nueva_cadena in numeros:
            print(f"El carácter '{nueva_cadena}' no se puede añadir a la lista.")
        else:
            self.cadena += nueva_cadena
        return self.cadena
    
    def __str__(self):
        return(str(self.cadena))
      
cadena1 = CadenaPerso("Ho,la")
print(cadena1)
cadena1 + ","
cadena1 + "."    
cadena2 = cadena1 + " ¿Cómo estás?"
print(cadena2)
        
            
            