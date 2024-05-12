class Rectangulo:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        
    def perimetro(self):
        return 2 * self.ancho + 2 * self.largo
    
    def superficie(self):
        return self.ancho * self.largo
    
