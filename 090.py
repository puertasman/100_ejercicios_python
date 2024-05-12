class Rectangulo:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        
    def perimetro(self):
        return 2 * self.ancho + 2 * self.largo
    
    def superficie(self):
        return self.ancho * self.largo
    
rectangulo1 = Rectangulo(10,15)
print(rectangulo1.ancho)
print(rectangulo1.largo)
print(rectangulo1.perimetro())
print(rectangulo1.superficie())