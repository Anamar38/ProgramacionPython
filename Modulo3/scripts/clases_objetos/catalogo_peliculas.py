# Se tienen 3 tiendas diferentes de peliculas. Cada tienda tiene su propio catalogo de peliculas dispuestas para alquilar

# La primera tienda tiene las siguientes peliculas en catalogo:
#     - Avatar
#     - Avatar 2

# La segunda tienda tiene las peliculas:
#     - El conjuto
#     - La monja

# La tercera tienda posse las peliculas
#     - Avengers
#     - Spiderman
#     - Hulk

# Usted es un cliente y desea ordenar una pelicula, solicite a cada tienda el listado de peliculas disponibles para el alquiler
# """

class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
    pass


class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)


#  creando 3 tiendas de peliculas

tienda1_catalogo = Catalogo(
    [Pelicula('Avatar', 210, 2010), Pelicula('Avatar2', 250, 2022)])
tienda2_catalogo = Catalogo(
    [Pelicula('El conjuro', 120, 2016), Pelicula('La monja', 90, 2018)])
tienda3_catalogo = Catalogo([Pelicula('Avengers', 120, 2012), Pelicula(
    'Spiderman', 110, 2003), Pelicula('Hulk', 100, 2006)])


print('Mostando catalogo de peliculas por tienda ...')

print('La primera tienda posse las siguientes peliculas para alquilar: ')
tienda1_catalogo.mostrar()

print('La segunda tienda posse las siguientes peliculas para alquilar: ')
tienda2_catalogo.mostrar()

print('La tercera tienda posse las siguientes peliculas para alquilar: ')
tienda3_catalogo.mostrar()
