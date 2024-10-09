## Lógica de conexión para la BD

from conexion import *

def InsertarLibro(p):
    db = client.libreria
    collection = db['libros']
    collection.insert_one(p)

def FilterLibro(search):
    db = client.libreria
    collection = db['libros']
    show_data_count = len(list(collection.find(search)))
    if show_data_count > 0:
        show_data = collection.find(search)
        for i in show_data:
            print(i)
    else:
        print("No existe el libro con los criterios ingresados")

def VizualizarLibro():
    db = client.libreria
    collection = db['libros']
    show_data = collection.find()
    for data in show_data:
        print(data)

def EliminarLibro(ISBN):
    db = client.libreria
    collection = db['libros']
    collection.delete_many({"ISBN": ISBN})

def ActualizarLibro(ISBN, update):
    db = client.libreria
    collection = db['libros']
    collection.update_one({"ISBN": ISBN}, {'$set': update})
