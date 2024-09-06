## Lógica de conexión para la BD

from conexion import *

def InsertarPersona(p):
    # si db no existe, esto lo crea 😎
    db = client.ejemplo1
    # db almacenala db en el cluster
    # client es el objeto que proporciona la conexion
    # ejemplo1 es el nombre de la db
    collection = db['Person'] # Selecciona la colección "Person"
    # insertamos un documento
    collection.insert_one(p)
    
def FilterAlumno(search):
    # conectamos con la db
    db = client.ejemplo1
    collection = db['Person']
    # find realiza una busqueda en la colleción usando el criterio "search"
    show_data_count = len(list(collection.find(search)))
    # agregar condicion para verificar existencia de los resultados
    if show_data_count > 0 :
        show_data = collection.find(search)
        # iteramos sobre los resultados para imprimir cada documento
        for i in show_data:
           print(i)
    else:
            print("No existe el rut ingresado") 

def VizualizarAlumno():
    db = client.ejemplo1
    collection = db['Person']
    show_data = collection.find()
    for data in show_data:
        print(data)
def EliminarAlumno(rut):
    db = client.ejemplo1
    collection = db['Person']
    collection.delete_many({"Rut": rut})

def ActualizarAlumno(rut, update):
    db = client.ejemplo1
    collection = db['Person']
    collection.update_one({"Rut": rut}, {'$set': update})

######################## COLECCION DE CURSO #########################################

def VizualizarCurso():
    db = client.ejemplo1
    collection = db['Curso']
    show_data = collection.find()
    for data in show_data:
        print(data)

def FilterCurso(search):
    # conectamos con la db
    db = client.ejemplo1
    collection = db['Curso']
    # find realiza una busqueda en la colleción usando el criterio "search"
    show_data_count = len(list(collection.find(search)))
    # agregar condicion para verificar existencia de los resultados
    if show_data_count > 0 :
        show_data = collection.find(search)
        # iteramos sobre los resultados para imprimir cada documento
        for i in show_data:
           print(i)
    else:
            print("No existe el código de curso ingresado") 

def ActualizarCurso(rut, update):
    db = client.ejemplo1
    collection = db['Curso']
    collection.update_one({"Rut_estudiante": rut}, {'$set': update})

def EliminarCurso(rut):
    db = client.ejemplo1
    collection = db['Curso']
    collection.delete_one({"Rut_estudiante": rut})
def InsertCurso(p):
    db = client.ejemplo1
    collection = db['Curso']
    collection.insert_one(p)