import os

ruta_completa = __file__
nombre_archivo = os.path.basename(ruta_completa)
extension_archivo = nombre_archivo.split('.')[-1]
print("Extension de archivo: ", extension_archivo)