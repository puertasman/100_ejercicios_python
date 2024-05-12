class Coche:
    def __init__ (self, marca='Peugeot', color='negro', nombreConductor='ninguno', kmInicio=16900):
        self.marca = marca
        self.color = color
        self.nombreConductor = nombreConductor
        self.kmInicio = kmInicio
        
    def seleccionConductor(self,nombreConductor):
        self.nombreConductor = nombreConductor
        
    def distanciaRecorrida(self, kmFin):
        if kmFin > self.kmInicio:   
            return kmFin - self.kmInicio
        else:
            return "No puede acabar en menos kilómetros que empezó"
    
    def mostrarInfo(self, kmActual):
        print(f"El coche es de marca {self.marca} y color {self.color}, el conductor es {self.nombreConductor}, tiene un kilometraje actual de {kmActual} km.")

coche1 = Coche()
coche1.seleccionConductor("Patrick")        
print(coche1.distanciaRecorrida(20000))
print(coche1.distanciaRecorrida(2000))
coche1.mostrarInfo(20000)
