# Archivo para llamar funciones que se encuentran en models.py
# tambien sirve para solicitar datos de entrada

from models import * 

# ingresamos datos

def Ingresar_libro():
    # solicita datos a n personas
    while True:
        ISBN = input("Ingrese el ISBN\n")
        if len(ISBN) > 0:
            break
        else:
            print("No ingresó un nombre válido. Intente nuevamente.")
    while True:
        titulo= input("Ingrese el titulo\n")
        if len(titulo) > 0:
            break
        else:
            print("No ingresó un nombre válido. Intente nuevamente.")        
    while True:
        autor= input("Ingrese el autor\n")
        if len(autor) > 0:
            break
        else:
            print("No ingresó un nombre válido. Intente nuevamente.")
    while True:
        año = input("Ingresa el año de publicación \n")
        if len(año) > 0:
            try:
                año = int(año)
                break
            except ValueError:
                print("No ingresó un número válido. Intente nuevamente.")
        else:
            print("No ingresó un año válido. Intente nuevamente.")
    while True:
        editorial = input("Ingrese la editoriala\n")
        if len(editorial) > 0:
            break
        else:
            print("No ingresó una carrera válida. Intente nuevamente.")
    while True:
        try:
            precio= int(input("Ingrese el precio\n"))
            if precio<0:
                print("No ingresó un precio válido. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("No ingresó un número válido. Intente nuevamente.")
    # fin de ingreso de datos
    # json para enviar el metodo de insercion
    p = {}
    if len(ISBN) > 0:
        p["ISBN"] = ISBN
    if len(titulo) > 0:
        p["Titulo"] = titulo
    if len(autor) > 0:
        p["Autor"] = autor
    if len(str(año)) > 0:
        p["Año"] = año
    if len(editorial) > 0:
        p["Editorial"] = editorial
    if len(str(precio)) > 0:
        p["Precio"] = precio
    ## fin de metodo insercion de datos
    InsertarLibro(p)
        
def Vizualizar_libro():
    VizualizarLibro()
#fin del ciclo para solicitar datos
def Filtro_libro():
    while True:
        try:
            opcion = int(input("""
                               1 Buscar por ISBN
                               2 Buscar por título
                               3 Buscar por autor
                               4 Buscar por año de publicación
                               5 Buscar por editorial
                               6 Buscar por precio
                               7 Salir
                               -->  """))
            search_criteria = {}
            if opcion == 1:
                search = input("Ingresa ISBN\n")
                search_criteria["ISBN"] = search
            elif opcion == 2:
                search = input("Ingresa título\n")
                search_criteria["Titulo"] = search
            elif opcion == 3:
                search = input("Ingresa autor\n")
                search_criteria["Autor"] = search
            elif opcion == 4:
                search = int(input("Ingresa año de publicación\n"))
                search_criteria["Año"] = search
            elif opcion == 5:
                search = input("Ingresa editorial\n")
                search_criteria["Editorial"] = search
            elif opcion == 6:
                search = int(input("Ingresa precio\n"))
                search_criteria["Precio"] = search
            elif opcion == 7:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                continue

            FilterLibro(search_criteria)
        except ValueError:
            print("\nVALOR INCORRECTO\n")

def Actualizar_libro():
    while True:
        ISBN = input("Ingrese el ISBN del libro a actualizar\n")
        if len(ISBN) > 0:
            break
        else:
            print("No ingresó un ISBN válido. Intente nuevamente.")

    update_fields = {}
    while True:
        titulo = input("Ingrese el nuevo título (deje en blanco para no cambiar)\n")
        if len(titulo) > 0:
            update_fields["Titulo"] = titulo
        break

    while True:
        autor = input("Ingrese el nuevo autor (deje en blanco para no cambiar)\n")
        if len(autor) > 0:
            update_fields["Autor"] = autor
        break

    while True:
        año = input("Ingrese el nuevo año de publicación (deje en blanco para no cambiar)\n")
        if len(año) > 0:
            try:
                año = int(año)
                update_fields["Año"] = año
            except ValueError:
                print("No ingresó un número válido. Intente nuevamente.")
        break

    while True:
        editorial = input("Ingrese la nueva editorial (deje en blanco para no cambiar)\n")
        if len(editorial) > 0:
            update_fields["Editorial"] = editorial
        break

    while True:
        precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar)\n")
        if len(precio) > 0:
            try:
                precio = int(precio)
                if precio < 0:
                    print("No ingresó un precio válido. Intente nuevamente.")
                else:
                    update_fields["Precio"] = precio
            except ValueError:
                print("No ingresó un número válido. Intente nuevamente.")
        break

    if update_fields:
        ActualizarLibro(ISBN, update_fields)
        print("Libro actualizado correctamente.")
    else:
        print("No se realizaron cambios.")
def Eliminar_libro():
    while True:
        ISBN = input("Ingrese el ISBN del libro a eliminar\n")
        if len(ISBN) > 0:
            break
        else:
            print("No ingresó un ISBN válido. Intente nuevamente.")
    EliminarLibro(ISBN)
    print("Libro eliminado correctamente.")
