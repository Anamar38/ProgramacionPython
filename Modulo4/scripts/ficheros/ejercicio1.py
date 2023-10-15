import os
from utils import ingreso_datos as ing


# https://note.nkmk.me/en/python-script-file-path/
path = os.path.dirname(__file__)


def generar_listado_escritura(n: int):
    lista_escribir = list()
    for i in range(1, 13):
        cadena = f'{i} x {n} = {i*n}\n'
        lista_escribir.append(cadena)
    return lista_escribir

# Solicitar al usuario un número entre 1 y 10

n = ing.ingreso_numero_entero('Ingrese un número del 1 al 10: ')
assert n<=10 and n>=1, 'El número debe estar entre 1 y 10'


lista_escribir = generar_listado_escritura(n)

# Generar la tabla de multiplicar y escribirla en un archivo
nombre_archivo =  os.path.join(path, f"tabla-{n}.txt") 

with open(nombre_archivo, 'w') as file:
    file.writelines(lista_escribir)
