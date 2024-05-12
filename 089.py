class Persona:
    def __init__(self, altura, peso, edad):
        self.altura = altura
        self.peso = peso
        self.edad = edad
        
    def calcularIMC(self):
        imc = self.peso/(self.altura**2)
        return imc
    
    def interpretacionIMC(self):
        imc = self.calcularIMC()
        if imc <= 18.5:
            print("El resultado del cálculo del IMC indica que la persona tiene bajo peso(delgadez).")
        elif imc >= 30:
            print("El resultado del cálculo del IMC indica que la persona es obesa.")
        else:
            print("La persona tiene sobrepeso o una complexión normal.")
   
julien = Persona(1.87,95,26)         
print(f"{julien.calcularIMC():.2f}")
julien.interpretacionIMC()
