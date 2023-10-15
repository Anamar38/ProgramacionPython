"""
Solicite el ingreso de alumnos y 3 notas. Registre los datos en una base de datos SQLite y en un archivo de texto.
"""

from utils.ingreso_datos import ingreso_numero_entero

import sqlite3
import os

os.chdir(os.path.dirname(__file__))


def creacion_tabla():
    
    with sqlite3.connect('colegio.db') as conexion:
        
        cursor = conexion.cursor()
        
        # Insertamos un registro en la tabla de usuarios
        sentencia = open('./src/tabla.sql', 'r').read()
        cursor.execute(sentencia)

        # Guardamos los cambios haciendo un commit
        conexion.commit()



def generar_listado_alumnos(n:int)->list:
    listado_alumnos = []
    for i in range(n):
        print(f'----- Ingreso datos Alumno {i+1} -------')

        dicx_alumno = {}

        dicx_alumno['nombre'] = input('Ingrese el nombre del alumno: ')
        dicx_alumno['nota1'] = ingreso_numero_entero('Ingrese la primera nota: ')
        dicx_alumno['nota2'] = ingreso_numero_entero('Ingrese la segunda nota: ')
        dicx_alumno['nota3'] = ingreso_numero_entero('Ingrese la tercera nota: ')
        listado_alumnos.append(dicx_alumno)

    return listado_alumnos


def main():
    # Solicita cantidad alumnos
    n = ingreso_numero_entero('Ingrese la cantidad de alumnos a registrar: ')
    assert n>0, ValueError('N debe ser mayor a 0')

    # genero listado de alumnos
    listado_alumnos= generar_listado_alumnos(n)

    # para guardar datos sobre la bd necesito un listado de tuplas
    listado_bd = [tuple(alumno.values()) for alumno in listado_alumnos]

    # creo tabla y bd en sqlite3
    creacion_tabla()

    # agrego contenido a tabla
    with sqlite3.connect('colegio.db') as conexion:
        cursor = conexion.cursor()

        # Ahora utilizamos el método executemany() para insertar varios
        cursor.executemany("INSERT INTO Alumnos VALUES (?,?,?, ?)", listado_bd)

        # Guardamos los cambios haciendo un commit
        conexion.commit()
        pass

    with sqlite3.connect('colegio.db') as conexion:
        cursor = conexion.cursor()

        # Recuperamos los registros de la tabla de usuarios
        cursor.execute("SELECT * FROM Alumnos")

        # Recorremos todos los registros con fetchall
        # y los volcamos en una lista de usuarios
        usuarios = cursor.fetchall()
        pass

    # Ahora podemos recorrer todos los usuarios
    for usuario in usuarios:
        print(usuario)

    

pass

if __name__ == '__main__':
    main()

















