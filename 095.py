class NumeroComplejo:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __str__(self):
        return(f"{self.real} + {self.img}i")
    
    def __repr__(self):
        return(f"valor de real: {self.real}\n valor de img: {self.img}")
    
num1 = NumeroComplejo(2,7)
print(num1)
print(repr(num1))