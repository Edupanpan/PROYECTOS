# Archivo para llamar funciones que se encuentran en models.py
# tambien sirve para solicitar datos de entrada

from models import * 

# ingresamos datos

def Ingresar_alumno():
    # solicita datos a n personas
    while True:
        nombre = input("Ingrese el nombre\n")
        if len(nombre) > 0:
            break
        else:
            print("No ingresó un nombre válido. Intente nuevamente.")
    while True:
        try:
            edad = int(input("Ingresa edad\n"))
            if edad < 0 or edad > 90:
                print("No ingresó una edad válida. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("No ingresó un número válido. Intente nuevamente.")
    while True:
        rut = input("Ingrese el rut\n")
        if len(rut) == 8 or len(rut) == 9:
            break
        else:
            print("No ingresó un rut válido. Intente nuevamente.")
    while True:
        carrera = input("Ingrese la carrera\n")
        if len(carrera) > 0:
            break
        else:
            print("No ingresó una carrera válida. Intente nuevamente.")
    while True:
        try:
            año_ingreso = int(input("Ingrese el año de ingreso\n"))
            if año_ingreso < 1900 or año_ingreso > 2022:
                print("No ingresó un año de ingreso válido. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("No ingresó un número válido. Intente nuevamente.")
    # fin de ingreso de datos
    # json para enviar el metodo de insercion
    p = {}
    if len(nombre) > 0:
        p["Nombre"] = nombre
    if len(str(edad)) > 0:
        p["Edad"] = edad
    if len(str(rut)) > 0:
        p["Rut"] = rut
    if len(carrera) > 0:
        p["Carrera"] = carrera
    if len(str(año_ingreso)) > 0:
        p["Año_ingreso"] = año_ingreso
    ## fin de metodo insercion de datos
    InsertarPersona(p)
        
def Vizualizar_alumno():
    VizualizarAlumno()
#fin del ciclo para solicitar datos
def Filtro_alumno():
    while True:
        try:
            opcion = int(input("""
                               1 Buscar por nombre
                               2 Buscar por edad
                               3 Buscar por rut
                               4 Buscar por carrera
                               5 Buscar por año de ingreso
                               6 Salir
                               -->  """))
            search_criteria = {}
            if opcion == 1:
                search = input("Ingresa nombre\n")
                search_criteria["Nombre"] = search
            elif opcion == 2:
                search = int(input("Ingresa edad\n"))
                search_criteria["Edad"] = search
            elif opcion == 3:
                search = input("Ingresa rut\n")
                search_criteria["Rut"] = search
            elif opcion == 4:
                search = input("Ingresa carrera\n")
                search_criteria["Carrera"] = search
            elif opcion == 5:
                search = int(input("Ingresa año de ingreso\n"))
                search_criteria["Año_ingreso"] = search
            elif opcion == 6:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                continue

            FilterAlumno(search_criteria)
        except ValueError:
            print("\nVALOR INCORRECTO\n")

def Actualizar_alumno():
    while True:
        rut = input("Ingrese el rut del alumno a actualizar\n")
        if len(rut) == 8 or len(rut) == 9:
            break
        else:
            print("No ingresó un rut válido. Intente nuevamente.")

    update_fields = {}
    while True:
        nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar)\n")
        if len(nombre) > 0:
            update_fields["Nombre"] = nombre
        break

    while True:
        edad = input("Ingrese la nueva edad (deje en blanco para no cambiar)\n")
        if len(edad) > 0:
            try:
                edad = int(edad)
                if edad < 0 or edad > 90:
                    print("No ingresó una edad válida. Intente nuevamente.")
                else:
                    update_fields["Edad"] = edad
            except ValueError:
                print("No ingresó un número válido. Intente nuevamente.")
        break

    while True:
        carrera = input("Ingrese la nueva carrera (deje en blanco para no cambiar)\n")
        if len(carrera) > 0:
            update_fields["Carrera"] = carrera
        break

    while True:
        año_ingreso = input("Ingrese el nuevo año de ingreso (deje en blanco para no cambiar)\n")
        if len(año_ingreso) > 0:
            try:
                año_ingreso = int(año_ingreso)
                if año_ingreso < 1900 or año_ingreso > 2022:
                    print("No ingresó un año de ingreso válido. Intente nuevamente.")
                else:
                    update_fields["Año_ingreso"] = año_ingreso
            except ValueError:
                print("No ingresó un número válido. Intente nuevamente.")
        break

    if update_fields:
        ActualizarAlumno(rut, update_fields)
        print("Alumno actualizado correctamente.")
    else:
        print("No se realizaron cambios.")
def Eliminar_alumno():
    while True:
        rut = input("Ingrese el rut del alumno a eliminar\n")
        if len(rut) == 8 or len(rut) == 9:
            break
        else:
            print("No ingresó un rut válido. Intente nuevamente.")
    EliminarAlumno(rut)
    print("Alumno eliminado correctamente.")


########################################## CURSO ##########################################################
def Ingresar_curso():
    while True:
        curso = input("Ingrese el curso\n")
        if len(curso) > 0:
            break
        else:
            print("No ingresó un curso válido. Intente nuevamente.")

    while True:
        codigo_curso = input("Ingrese el código del curso\n")
        if len(codigo_curso) > 0:
            break
        else:
            print("No ingresó un código de curso válido. Intente nuevamente.")

    while True:
        rut_estudiante = input("Ingrese el rut del estudiante\n")
        if len(rut_estudiante) == 8 or len(rut_estudiante) == 9:
            break
        else:
            print("No ingresó un rut válido. Intente nuevamente.")

    while True:
        try:
            nota_final = float(input("Ingrese la nota final\n"))
            if nota_final < 1 or nota_final > 7:
                print("No ingresó una nota final válida. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("No ingresó un número válido. Intente nuevamente.")

    # fin de ingreso de datos
    # json para enviar el método de inserción
    p = {}
    if len(curso) > 0:
        p["Curso"] = curso
    if len(codigo_curso) > 0:
        p["Codigo_curso"] = codigo_curso
    if len(rut_estudiante) > 0:
        p["Rut_estudiante"] = rut_estudiante
    if len(str(nota_final)) > 0:
        p["Nota_final"] = nota_final
    ## fin de método inserción de datos

    InsertCurso(p)

def Vizualizar_curso():
    VizualizarCurso()

def Filtro_curso():
    while True:
        try:
            opcion = int(input("""
                               1 Buscar por curso
                               2 Buscar por código de curso
                               3 Buscar por rut
                               4 Salir
                               -->  """))
            search_criteria = {}
            if opcion == 1:
                search = input("Ingresa curso\n")
                search_criteria["Curso"] = search
            elif opcion == 2:
                search = input("Ingresa código de curso\n")
                search_criteria["Codigo_curso"] = search
            elif opcion == 3:
                search = input("Ingresa rut\n")
                search_criteria["Rut_estudiante"] = search
            elif opcion == 4:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                continue

            FilterCurso(search_criteria)
        except ValueError:
            print("\nVALOR INCORRECTO\n")

def Actualizar_curso():
    while True:
        rut = input("Ingrese el rut del alumno a actualizar\n")
        if len(rut) == 8 or len(rut) == 9:
            break
        else:
            print("No ingresó un rut válido. Intente nuevamente.")

    update_fields = {}
    while True:
        curso = input("Ingrese el nuevo curso (deje en blanco para no cambiar)\n")
        if len(curso) > 0:
            update_fields["Curso"] = curso
        break
    while True:
        codigo_curso = input("Ingrese el codigo del nuevo curso (deje en blanco para no cambiar)\n")
        if len(codigo_curso) > 0:
            update_fields["Codigo_curso"] = codigo_curso
        break

    while True:
        nota = input("Ingrese la nueva nota (deje en blanco para no cambiar)\n")
        if len(nota) > 0:
            try:
                nota = float(nota)
                if nota < 1 or nota > 7:
                    print("No ingresó una nota válida. Intente nuevamente.")
                else:
                    update_fields["Nota_final"] = nota
            except ValueError:
                print("No ingresó un número válido. Intente nuevamente.")
        break

    if update_fields:
        ActualizarCurso(rut, update_fields)
        print("Curso actualizado correctamente.")
    else:
        print("No se realizaron cambios.")
def Eliminar_curso():
    while True:
        rut = input("Ingrese el rut del alumno a eliminar curso\n")
        if len(rut) == 8 or len(rut) == 9:
            break
        else:
            print("No ingresó un rut válido. Intente nuevamente.")
    EliminarCurso(rut)
    print("Curso eliminado correctamente.")
        
# fin del ciclo para solicitar datos