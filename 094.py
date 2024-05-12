class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Se acaba de crear el punto ({self.x},{self.y})")
        
    def __add__(self, p):
        suma = Punto2D(self.x + p.x, self.y + p.y)  # creando punto
        #print (tuple((self.x + p.x, self.y + p.y)))  #sólo retornando el valor
        
    
    def __sub__(self, p):
        print (tuple((self.x - p.x, self.y - p.y)))
    
    def __mul__(self, p):
        print (tuple((self.x * p.x, self.y * p.y)))
    
    def __truediv__(self, p):
        print (tuple((self.x / p.x, self.y / p.y)))
    
    
p1 = Punto2D(3,2)
p2 = Punto2D(1,4)

p1+p2
p1-p2
p1*p2
p1/p2