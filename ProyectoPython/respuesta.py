import random
import pymongo
import mongodb

ahorcado = mongodb.db.coleccion.aggregate([{ "$sample": { "size": 1 } }]).next()
respuesta = ahorcado["Nombre"]

print(respuesta)