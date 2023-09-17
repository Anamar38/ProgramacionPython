# Crear un programa que permita decidir a una persona cruzar la calle o no según:
# - Si semáforo esta en verde cruzar la calle
# - Si semáforo esta en rojo o amarillo no cruzar

# La persona debe poder ingresar el estado del semáforo por teclado



estado_semaforo = input("Ingresa el estado del semaforo: ")
estado_semaforo = estado_semaforo.lower()


if estado_semaforo == "verde":
    print("Cruza la calle")
elif estado_semaforo == "rojo" or estado_semaforo == "amarillo":
    print("No cruces")
else :
    print("Estado no registrado")


print('Programa finalizado!!!')