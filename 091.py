from b090 import Rectangulo
class Paralepipedo(Rectangulo):
    def __init__(self, ancho, largo, altura):
        super().__init__(ancho, largo)
        self.altura = altura
        
    def volumen(self):
        return self.superficie() * self.altura
    
paralepipedo1 = Paralepipedo(9,5,2)
print(paralepipedo1.perimetro())
print(paralepipedo1.superficie())
print(paralepipedo1.volumen())