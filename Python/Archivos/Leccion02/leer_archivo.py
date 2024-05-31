archivo = open('c:\\prueba.txt','r', 
               encoding='utf8') #Las letras son: 'r' read, 'a' append, 'w' write, x
#print(archivo.read())
#print(archivo.read(16))
#print(archivo.read(10)) # Continuamos desde la linea anterior
#print(archivo.readline())
#print(archivo.readline())

# vamos a iterar el archivo, cada una de las lineas
for linea in archivo:
#print(linea): iteramos todos los elementos del archivo
#print(archivo.readlines()[11]) # accedemos al archivo como si fuera una lista

#Anexamos informaciuon; copiamos a otro.
  archivo2 = open('copia.txt','w', encoding='utn8')
  archivo2.write(archivo.read())
  archivo.close() # cerramos el primer archivo
  archivo2.close() # cerramos el segundun archivo
  
  print('se ha terminado el proceso de leer y copiar archivo ')
  
