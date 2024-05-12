class CuentaBancaria():
    def __init__(self, nombre="Maxime", saldo=600):
        self.nombre = nombre
        self.saldo = saldo
    
    def deposito(self, cantidad):
        self.saldo += cantidad
    
    def retiro(self, cantidad):
        self.saldo -= cantidad
        
    def __repr__(self):
        return f"El saldo de la cuenta bancaria de {self.nombre} es de {self.saldo} euros."
    
cuenta1 = CuentaBancaria('Julie',1000)
cuenta1.deposito(400)
cuenta1.retiro(100)
print(cuenta1)

        
cuenta2 = CuentaBancaria()
cuenta2.deposito(500)
print(cuenta2)