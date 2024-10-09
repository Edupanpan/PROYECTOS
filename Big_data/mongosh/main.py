# lanza la aplicación y funciona como interfaz de usuario

from funciones import *

def Seleccionar_opcion_libro():
    while True:
        try:
            opcion = int(input("""
                               1 Para Ingresar
                               2 Para Vizualizar datos
                               3 Para Busqueda por filtro
                               4 Para Actualizar datos
                               5 Para Eliminar datos 
                               6 Menu Principal
                               
                               -->  """))
            if opcion == 1:
                Ingresar_libro()
            elif opcion == 2:
                Vizualizar_libro()
            elif opcion == 3:
                Filtro_libro()
            elif opcion == 4:
                Actualizar_libro()
            elif opcion == 5:
                Eliminar_libro()
            elif opcion == 6:
                break
        except ValueError:
            print("\nVALOR INCORRECTO\n")

def Main():
    while True:
        try:
            opcion = int(input("""
                               1 Para Libros
                               2 Para salir
                               
                               -->  """))
            if opcion == 1:
                Seleccionar_opcion_libro()
            elif opcion == 2:
                break
        except ValueError:
            print("\nVALOR INCORRECTO\n")

Main()
