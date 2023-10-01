"""
Crear un programa Menu que contenga las siguientes funcionalidades:

1. Realizar la suma de 2 número
2. Imprimir un triangulo rectangulo de altura h elaborado por #
3. Calcular el factorial de un número n
4. Realizar el ingreso de datos de n alumnos y sus notas
5. Salir
"""

# 1. Librerias
from pprint import pprint


# 1.2 librerias creadas
from utils import ingreso_datos as ing
from utils.diversos import mostrar_triangulo, calcular_factorial_recursivo
from utils.alumnos import ingreso_listado_alumnos

# 2. Constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """
¿Qué quieres hacer? 
    1) Realizar la suma de 2 número
    2) Imprimir un triangulo rectangulo de altura h elaborado por #
    3) Calcular el factorial de un número n
    4) Realizar el ingreso de datos de n alumnos y sus notas
    5) Salir

Escribe una opción: """


# 3. Funciones y /o metodos

def sumar(x, y):
    return x + y


def opcion1():
    x = ing.ingreso_numero_decimal('Ingrese el primeor número: ')
    y = ing.ingreso_numero_decimal('Ingrese el segundo número: ')
    suma = sumar(x,y)
    print(f'{x} + {y} = {suma}')


def opcion2():
    h = ing.ingreso_numero_entero('Ingrese la altura del triangulo: ')
    assert h >=1, 'La altura del triangulo debe ser un número positivo'

    mostrar_triangulo(h)


def opcion3():
    n = ing.ingreso_numero_entero('Ingrese el número del factorial a calcular: ')
    if n<0:
        raise Exception(f'No se comtempla calculo de factoriales negativos. Valor ingresado es {n}')

    fac = calcular_factorial_recursivo(numero=n)
    print(f'{n}! = {fac}')

def opcion4():
    listado_alumnos = ingreso_listado_alumnos()
    print('-------- Se genero el siguiente listado de alumnos ------- ')
    pprint(listado_alumnos)



def main():
    print(MENSAJE_BIENVENIDA)
    while True:
        opcion = input(OPCIONES_MENU)
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            opcion4()
        elif opcion =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# 4. Main
if __name__ == '__main__':
    main()


