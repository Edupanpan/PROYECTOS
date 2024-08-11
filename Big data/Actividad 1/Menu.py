from BD import creacion, filtrar,agregar, modificar
def menu():     
        print("""
                                Bienvenido al gestor de 'Pandas'
                                
                                Que desea realizar:
                                1.-Mostrar datos
                                2.-Filtrar datos
                                3.-Agregar datos
                                4.-Modificar datos
                                5.-Salir
                                """)
def opciones(seleccion):
        if seleccion==1:
                creacion()
        elif seleccion==2:
                filtrar()   
        elif seleccion==3:
                agregar()
        elif seleccion==4:
                modificar()
        elif seleccion==5:
                print("Hasta luego")
                exit
                return False
        else:
                print("ingrese valor valido")
        return True
def main():
        flag=True
        while flag:
                menu()
                seleccion=int(input(":"))
                flag=opciones(seleccion)

