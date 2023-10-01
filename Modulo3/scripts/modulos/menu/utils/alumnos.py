from .ingreso_datos import ingreso_numero_decimal

def ingreso_listado_alumnos() -> list:
    """Permite generar un listado de alumnos"""

    listado_alumnos = list()
    bool_ingreso = True
    while bool_ingreso:

        # realizo ingreso de datos
        dicx_alumno = {}
        nombre_alumno = input('Ingrese el nombre del alumno: ')

        notas = list()
        for i in range(3):
            nota = ingreso_numero_decimal(f'Ingrese la {i} nota: ')
            notas.append(nota)

        # agrego a diccionario
        dicx_alumno['nombre'] = nombre_alumno
        dicx_alumno['notas'] = notas

        listado_alumnos.append(dicx_alumno)

        respuesta = input('Desea agregar un nuevo alumno al listado?(y/n): ')
        if respuesta.lower() == 'n':
            bool_ingreso=False
    return listado_alumnos


if __name__ == '__main__':
    print(ingreso_listado_alumnos())