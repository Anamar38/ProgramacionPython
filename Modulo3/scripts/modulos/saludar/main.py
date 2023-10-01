
# import <nombre_archivo.py>  
# nombre_archivo -> nombre del archivo que contiene mis métodos a ser invocados
import paquete

# from <nombre_archivo> import <funcion/clase a emplear>
from paquete import saludar

# from <nombre_archivo> import * 
# * -> trae todas las funciones el archivo 
from paquete import *


paquete.saludar()
paquete.adios()


saludar()
adios()