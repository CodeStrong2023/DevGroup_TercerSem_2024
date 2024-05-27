import pymongo

try:
    # Conectarse a MongoDB (reemplaza con tus detalles de conexión)
    cliente = pymongo.MongoClient("mongodb+srv://DevGroup:ElMejorDeLaTecnicatura@clusterxxb.fwd8kw8.mongodb.net/")

    # Crea o busca la base de datos "pruebaProyecto" 
    db = cliente["Usuarios"] 

    # Crea la colección "animales"
    coleccion_nombre = db["Nombre"]
    coleccion_puntaje = db["Puntaje"]
    
    # Solicitar al usuario ingresar un nombre
    nombre = input("Ingrese el nombre: ")

    # Insertar el nombre en la colección "Nombre"
    resultado = coleccion_nombre.insert_one({"nombre": nombre})
    print(f"Nombre insertado con ID: {resultado.inserted_id}")

except Exception as e:
    print("Error al conectar a MongoDB:", e)
