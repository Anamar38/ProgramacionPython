"""
En este ejercicio deberás crear un script llamado personas.py
 que lea los datos de un fichero de texto, que transforme cada fila en un diccionario 
 y lo añada a una lista llamada personas. Luego rocorre las personas de la lista y para cada 
 una muestra de forma amigable todos sus campos.
"""

import os
from pprint import pprint

# cambiando directorio de trabajo
os.chdir(os.path.dirname(__file__))




# listado_lineas = open('personas.txt').readlines()
# listado_personas = []
# for linea in listado_lineas:
#     persona_dicx = dict()
#     x = linea.strip().split(';')

#     persona_dicx['id'] = x[0]
#     persona_dicx['nombre'] = x[1]
#     persona_dicx['apellido'] = x[2]
#     persona_dicx['fecha_nacimiento'] = x[3]

#     listado_personas.append(persona_dicx)


# pprint(listado_personas)





import csv

with open('personas.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["id"]}\n{row["nombre"]}, {row["apellido"]}\n{row["fecha_nacimiento"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

# print(csv_reader)