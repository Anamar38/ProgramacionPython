

def mostrar_triangulo(h:int):
    for i in range(h):
        print('#' * (i+1))



def calcular_factorial_recursivo(numero: int)-> int:
    """Calcula el factorial de un número de formar recursiva"""
    if numero == 0:
        return 1
    return calcular_factorial_recursivo(numero - 1) * numero