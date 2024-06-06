import pymongo
import random

try:
    # Conectarse a MongoDB (reemplaza con tus detalles de conexión)
    cliente = pymongo.MongoClient("mongodb+srv://DevGroup:ElMejorDeLaTecnicatura@clusterxxb.fwd8kw8.mongodb.net/")

    # Crea o busca la base de datos "pruebaProyecto" 
    db = cliente["Animales"] 
    dbUsers = cliente["Usuarios"]

    # Lista todas las colecciones en la base de datos
    colecciones = db.list_collection_names()
    
    listaUsuarios = dbUsers["listaUsuarios"]
       

    
    # Crear una variable donde se va a almacenar una colleccion aleatoria.
    if colecciones:
        # Seleccionar una colección aleatoria de la lista
        coleccion = random.choice(colecciones)

        
    coleccion_aleatoria = db[coleccion]
        
    animalDoc = coleccion_aleatoria.aggregate([{ "$sample": { "size": 1 } }]).next()
    animal = animalDoc["Nombre"] 
    # Busca animales en la base de datos




except Exception as e:
    print("Error al conectar a MongoDB:", e)

