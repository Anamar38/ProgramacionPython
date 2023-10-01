# la clase me sirve de molde para crear objetos
class Customer:
    def __init__(self, nombre, correo, phone) -> None:

        # variables inicializadoras para mi clase
        self.nombre_persona = nombre
        self.correo = correo
        self.telefono = phone
        pass

    def place_order(self):
        print('Relizando un pedido')
    
    def cancel_order(self):
        print('Cancela el pedido')


# creando al objeto lara
obj_1 = Customer('lara', 'lara@company.com', '84351313')

print('Se creo el objeto : ', obj_1.nombre_persona)

obj_1.place_order()
obj_1.cancel_order()

# Creando el objeto tess
obj_2 = Customer('tess', 'tess@company.com', '65453131')
print('Se creo el objeto : ', obj_2.nombre_persona)
obj_2.place_order()