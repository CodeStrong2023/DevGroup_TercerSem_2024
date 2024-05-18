import pymongo

try:
    # Conectarse a MongoDB (reemplaza con tus detalles de conexión)
    cliente = pymongo.MongoClient("mongodb+srv://DevGroup:ElMejorDeLaTecnicatura@clusterxxb.fwd8kw8.mongodb.net/")

    # Crea o busca la base de datos "pruebaProyecto" 
    db = cliente["Animales"] 

    # Crea la colección "animales"
    coleccion_animal = db["Mamíferos"]

    # Crear una variable donde se va a almacenar una colleccion aleatoria.
    coleccion = 0 # cambiar para encontrar una aleatoria.

    # Busca animales en la base de datos




except Exception as e:
    print("Error al conectar a MongoDB:", e)

