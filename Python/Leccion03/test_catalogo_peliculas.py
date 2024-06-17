from catalogo_peliculas.dominio.Pelicula import Pelicula
from catalogo_peliculas.servicio.catalogo_peliculas import catalogopeliculas as CP


opcion = None
while opcion  != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Peliculas')
        print('2. Listar las peliculas')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input('Digite una opcion de menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input("Digite el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            CP.agregar_peliculas(pelicula)
        elif opcion == 2:
            CP.listar_peliculas()
        elif opcion == 3:
            CP.eliminar_peliculas()
    except Exception as e:
        print(f'ocurrió un error de tipo: {e}')
        opcion = None 
    else:
        print('Salimos del programa')
        