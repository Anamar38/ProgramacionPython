
from utils import ingreso_datos as ing
import os


path = os.path.dirname(__file__)

def main():
    n = ing.ingreso_numero_entero('Ingrese un número del 1 al 10: ')

    if n>10 and n<1:
        raise ValueError('El número debe estar entre 1 y 10')

    try:
        nombre_archivo =  os.path.join(path, f"tabla-{n}.txt") 
        data = open(nombre_archivo).read()
        print(data)
    except FileNotFoundError:
        print("EL archivo no existe")

    pass



if __name__ =='__main__':

    main()



