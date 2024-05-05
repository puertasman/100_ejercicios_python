from datetime import datetime

def numDiasHoras(fechaInicio, fechaFin):
    formato_fecha = "%Y/%m/%d"
    
    fecha_inicio = datetime.strptime(fechaInicio, formato_fecha)
    fecha_fin = datetime.strptime(fechaFin, formato_fecha)
    numDias = (fecha_fin - fecha_inicio).days
    numHoras = numDias * 24
    return numDias, numHoras
    
print(numDiasHoras("2022/05/15","2022/06/20"))

print(numDiasHoras("2022/04/1","2022/04/27"))