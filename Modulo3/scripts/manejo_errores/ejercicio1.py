"""Del ejercicio 6 modulo2/funciones escribir un código que permita el ingreso de datos del número n y p empleando manejo de errores

Probar mediante assert que el valor de p sea diferente a 0

"""


def calcular_k_suma_recursiva(n:int, p: int)->int:
    """
    Retorna el valor de la funcion 
    K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p 
    """
    if n == 1:
        return 1 * p
    return calcular_k_suma_recursiva(n-1, p) + n * p


def ingreso_numero_entero(msg:str = 'Ingrese un número entero: ')->int:
    try:
        x = int(input(msg))
        return x
    except:
        return ingreso_numero_entero(msg)


n = ingreso_numero_entero('Ingrese el número n: ')
# si n, no es número natural entonces genero una excepción
if n<=0:
    raise Exception(f' "n" debe ser un número natural. El número ingresado fue {n}')

p = ingreso_numero_entero('Ingrese el número p: ')
assert p != 0, 'El valor de p debe ser distinto a 0'

x = calcular_k_suma_recursiva(n,p)
print(f'k({n}, {p}) = {x}')