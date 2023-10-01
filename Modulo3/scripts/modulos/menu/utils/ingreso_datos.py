

def ingreso_numero_entero(msg:str = 'Ingrese un número entero: ')->int:
    try:
        x = int(input(msg))
        return x
    except:
        return ingreso_numero_entero(msg)
    
def ingreso_numero_decimal(msg:str = 'Ingrese un número decimal: ')->float:
    try:
        x = float(input(msg))
        return x
    except:
        return ingreso_numero_decimal(msg)