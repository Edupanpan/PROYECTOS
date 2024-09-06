# lanza la aplicación y funciona como interfaz de usuario

from funciones import *
def Seleccionar_opcion_alumno():
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
                Ingresar_alumno()
            elif opcion == 2:
                Vizualizar_alumno()
            elif opcion == 3:
                Filtro_alumno()
            elif opcion == 4:
                Actualizar_alumno()
            elif opcion == 5:
                Eliminar_alumno()
            elif opcion == 6:
                break
        except:
            print ("\nVALOR INCORRECTO\n") 
def Seleccionar_opcion_curso():
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
                Ingresar_curso()
            elif opcion == 2:
                Vizualizar_curso()
            elif opcion == 3:
                Filtro_curso()
            elif opcion == 4:
                Actualizar_curso()
            elif opcion == 5:
                Eliminar_curso()
            elif opcion == 6:
                break
        except:
            print ("\nVALOR INCORRECTO\n") 
def Main():
    while True:
        try:
            opcion = int(input("""
                               1 Para Estudiantes
                               2 Para Cursos
                               3 Para salir
                               
                               -->  """))
            if opcion == 1:
                Seleccionar_opcion_alumno()
            elif opcion == 2:
                Seleccionar_opcion_curso()
            elif opcion == 3:
                break
        except:
            print ("\nVALOR INCORRECTO\n")
Main()
