# Encontrar todos los número primos desde el 1 al 100

def validar_numero_primo(numero:int):
    es_primo = True
    for i in range(2, numero):
        # validar si número es divisor
        if numero % i == 0:
            es_primo = False
    return es_primo

listado_primos = []
for numero_entero in range(1, 100):
    if validar_numero_primo(numero_entero):
        listado_primos.append(numero_entero)

print(listado_primos)

# evaluar si número 8 es primo
numero_entero = 8
es_primo = validar_numero_primo(numero_entero)
if es_primo:
    print(f'El número {numero_entero} es primo')
else:
    print(f'Número {numero_entero} no es primo')


