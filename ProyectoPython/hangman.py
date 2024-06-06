import random
import unicodedata
import mongodb
import pymongo
import googleapi as chatbot
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



# Función para la ventana principal del juego
def inicio():
    portadaLabel.pack(side="left")
    boton_iniciar.place(relx=0.81, rely=0.29, anchor=tk.CENTER)
    boton_registro.place(relx=0.81, rely=0.2, anchor=tk.CENTER)
    boton_clasificacion.place(relx=0.81, rely=0.38, anchor=tk.CENTER)
    boton_salir.place(relx=0.81, rely = 0.8, anchor=tk.CENTER)
    boton_reglas.place(relx=0.81, rely=0.47, anchor=tk.CENTER)
    if label_login.winfo_ismapped():
        label_login.place_forget()
    if label_password.winfo_ismapped():
        label_password.place_forget()
    if entradaLogin.winfo_ismapped():
        entradaLogin.place_forget()
    if entradaPassword.winfo_ismapped():
        entradaPassword.place_forget()
    if boton_volver.winfo_ismapped():
        boton_volver.place_forget()
    if boton_iniciarsesion.winfo_ismapped():
        boton_iniciarsesion.place_forget()
    if boton_registrar.winfo_ismapped():
        boton_registrar.place_forget()


# Funcion accionada por el boton "Iniciar Sesion"
def login():
    boton_iniciar.place_forget()
    boton_registro.place_forget()
    boton_salir.place_forget()
    boton_clasificacion.place_forget()
    boton_reglas.place_forget()
    label_login.place(relx=0.72, rely=0.4, anchor=tk.CENTER)
    entradaLogin.place(relx=0.825, rely=0.4, anchor=tk.CENTER)
    label_password.place(relx=0.72, rely=0.44, anchor=tk.CENTER)
    entradaPassword.place(relx=0.825, rely=0.44, anchor=tk.CENTER)
    boton_iniciarsesion.place(relx=0.78, rely=0.5, anchor=tk.CENTER)
    boton_volver.place(relx=0.78, rely=0.54, anchor=tk.CENTER)
    
# Funcion accionada por el boton "Registro"
def registro():
    boton_iniciar.place_forget()
    boton_registro.place_forget()
    boton_salir.place_forget()
    boton_clasificacion.place_forget()
    boton_reglas.place_forget()
    label_login.place(relx=0.72, rely=0.4, anchor=tk.CENTER)
    entradaLogin.place(relx=0.825, rely=0.4, anchor=tk.CENTER)
    label_password.place(relx=0.72, rely=0.44, anchor=tk.CENTER)
    entradaPassword.place(relx=0.825, rely=0.44, anchor=tk.CENTER)
    boton_registrar.place(relx=0.78, rely=0.5, anchor=tk.CENTER)
    boton_volver.place(relx=0.78, rely=0.54, anchor=tk.CENTER)


# Funcion para crear un usuario
def crear_usuario():
    usuario = entradaLogin.get("1.0","end-1c").strip()
    password = entradaPassword.get().strip()
    comprobar = tk.Label(ventana, text="", font=("Arial", 9, "bold"), bg="#1e396b", fg="#f6f6f6")

    def ocultar_mensaje():
        comprobar.place_forget()

    try:
        # Verifica si el usuario ya existe
        usuario_existente = mongodb.listaUsuarios.find_one({"Nombre": usuario.upper()})
        if usuario_existente:
            comprobar.config(text="El nombre de usuario ya existe.")
            comprobar.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
            ventana.after(2000, ocultar_mensaje)
            return
    
        # Inserta un nuevo usuario si no existe
        nuevo_usuario = mongodb.listaUsuarios.insert_one({"Nombre" : usuario.upper(),"Contraseña" : password, "Puntaje" : 0, "Palabras Acertadas" : 0})
        if nuevo_usuario.inserted_id:
            entradaLogin.place_forget()
            label_password.place_forget()
            entradaPassword.place_forget()
            label_login.place_forget()
            boton_registrar.place_forget()
            comprobar.config(text=f"Usuario {usuario} creado correctamente.")
            comprobar.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
            ventana.after(1500, inicio, comprobar.place_forget())
    except:
        comprobar.config(text="ERROR. No se pudo crear el usuario.")
        comprobar.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

usuario = "" # Variable global donde guardaremos el usuario que se ingese por teclado
usuarioDoc = [] # Aqui es donde luego guardaremos el documento de dicho usuario

# Funcion para comprobar si el usuario ingresado existe, en caso True, se logea dicho usuario
def comprobar_usuarios():
    global usuario
    global usuarioDoc
    # Entradas para el nombre y contraseña del usuario
    usuario = entradaLogin.get("1.0","end-1c").strip()
    password = entradaPassword.get().strip()
    
    # Comprobamos si el usuario existe
    if mongodb.dbUsers.listaUsuarios.find_one({"Nombre" : usuario.upper(), "Contraseña" : password}):
        usuarioDoc = mongodb.listaUsuarios.find_one({"Nombre" : usuario.upper()})
        entradaLogin.place_forget()
        label_password.place_forget()
        entradaPassword.place_forget()
        label_login.place_forget()
        boton_iniciarsesion.place_forget()
        label_bienvenida.config(text=f"Bienvenido {usuario}", font=("Arial", 9, "bold"))
        label_bienvenida.place(relx=0.5,rely=0.4, anchor=tk.CENTER)
        ventana.after(2000, iniciar_juego)
    else:
        label_bienvenida.config(text="USUARIO O CONTRASEÑA INCORRECTOS", font=("Arial", 9, "bold"))
        entradaLogin.place_forget()
        label_password.place_forget()
        entradaPassword.place_forget()
        label_login.place_forget()
        boton_iniciarsesion.place_forget()
        label_bienvenida.place(relx=0.8,rely=0.4, anchor=tk.CENTER) 
    
# Funcion para normalizar las cadenas de texto (Eliminar tildes)
def normalizar (cadena):
    resultado = []
    for c in cadena:
        if c.upper() == "Ñ":
            resultado.append(c)
        else:
            d = unicodedata.normalize("NFD", c)
            filtro = "".join(f for f in d if unicodedata.category(f) != "Mn") # Filtramos los caracteres con acentos
            c = unicodedata.normalize("NFC", filtro)
            resultado.append(c)
    return " ".join(resultado)

#Variables GLOBALES
puntaje = 200 # Variable para el puntaje
response = chatbot.model.generate_content(f'Generame una pista breve y no tan obvia sobre que animal es sin decirme su nombre {mongodb.animal}')
historial = []
historial.append({"Role" : "IA", "Mensaje" : response.text}) # Aqui guardamos el historial de pistas generadas por el chat
palabra_randomN = mongodb.animal.upper() # Variable donde almacenamos la palabra random
palabra_random = normalizar(palabra_randomN)
palabra = ["_"] * len(palabra_random) # Lista del largo de la palabra aleatoria (sera mostrada en el progreso del juego)
palabra_random_lista = list(palabra_random)
intentos = 0 # variable para los intentos fallidos
pista = 0 # Variable para el numero de pistas pedidos
for i in range(len(palabra_random)):
                if palabra_random_lista[i] == " ":
                    palabra[i] = " "
# ALIMENTACION
def entrada():
    # Aqui guardamos lo que el usuario ingrese por teclado
    pregunta =  normalizar(entradaAlimentacion.get("1.0","end-1c").upper().strip())
    # Llamamos a las variables globales que utilizaremos dentro de la funcion
    global intentos
    global puntaje
    global usuarioDoc
    UsuarioID = usuarioDoc["_id"] # Variable para obtener el id del usuario logeado
    
    # Lógica del juego
    if len(pregunta) == 1:
        if pregunta in palabra_random:
            for i in range(len(palabra_random)):
                if palabra_random_lista[i] == pregunta:
                    palabra[i] = pregunta
            actualizar_progreso(palabra) 
        else:
            intentos +=1
            if intentos <6:
                puntaje -= 20
                progreso_puntaje.config(text=f'Puntaje Actual: {puntaje}')
    else:
        if pregunta == palabra_random:
            progreso_label.config(text=f"¡Ganaste! \n La palabra era: {palabra_random}")
            if pista == 0:
                puntaje += 200
            progreso_puntaje.config(text=f"Felicidades! Has ganado {puntaje} puntos!")
            mongodb.listaUsuarios.update_one({"_id" : UsuarioID},  { "$inc": {"Palabras Acertadas": 1}})
            mongodb.listaUsuarios.update_one({"_id" : UsuarioID},  { "$inc": {"Puntaje" : puntaje}})
            print(usuarioDoc)
        else:
            intentos += 1
            if intentos < 6:
                puntaje -= 20
                progreso_puntaje.config(text=f'Puntaje Actual: {puntaje}')
    
    # Actualizar estado de intentos
    if intentos == 1:
                ahorcado1Label.place_forget()
                ahorcado2Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 2:
        ahorcado2Label.place_forget()
        ahorcado3Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 3:
        ahorcado3Label.place_forget()
        ahorcado4Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 4:
        ahorcado4Label.place_forget()
        ahorcado5Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 5:
        ahorcado5Label.place_forget()
        ahorcado6Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
        
                    
    # Chequear si el juego ha terminado
    if "".join(palabra) == palabra_random:
            progreso_label.config(text=f"¡Ganaste! \n La palabra era: {palabra_random}")
            if pista == 0:
                puntaje += 200
            progreso_puntaje.config(text=f"Felicidades! Has ganado {puntaje} puntos!")
            mongodb.listaUsuarios.update_one({"_id" : UsuarioID},  { "$inc": {"Palabras Acertadas": 1}})
            mongodb.listaUsuarios.update_one({"_id" : UsuarioID},  { "$inc": {"Puntaje" : puntaje}})
    elif intentos >= 6:
            progreso_label.config(text=f"Perdiste. La palabra era: {palabra_random}")

    entradaAlimentacion.delete(1.0, tk.END) # BORRA LOS TEXTOS INGRESADOS




# Crear la función para actualizar el label de progreso
def actualizar_progreso(palabra):
    progreso_label.config(text=" ".join(palabra))

    
# Funcion para mostrar el contenido del juego
def iniciar_juego():
    # Mostrar todos los widgets del juego
    progreso_label.place(relx=0.51, rely=0.25, anchor=tk.CENTER)
    boton_enviar.place(relx=0.51, rely=0.93, anchor=tk.CENTER)
    entradaAlimentacion.place(relx=0.51, rely=0.8, anchor=tk.CENTER)
    boton_mostrar_pista.place(relx=0.51, rely=0.72, anchor=tk.CENTER)
    boton_reiniciar_juego.place(relx=0.71, rely=0.93, anchor=tk.CENTER)
    ahorcado1Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    progreso_puntaje.place(relx=0.51, rely=0.85, anchor=tk.CENTER)
    HANGMANlabel.place(relx= 0.51, rely=0.15, anchor=tk.CENTER)

    # Ocultar el botón "Iniciar"
    portadaLabel.pack_forget()
    label_bienvenida.place_forget()
    boton_volver.place_forget()
    boton_iniciar.place_forget()
    
def mostrar_pista():
    global pista
    pista += 1
    pista_texto = historial[0]
    pista_texto = pista_texto["Mensaje"]
    # Mostrar la pista la ventana de respuesta
    respuesta_texto.insert(tk.END, f"{pista_texto}\n")
    # Deshabilitar el widget para hacerlo de solo lectura
    respuesta_texto.config(state=tk.DISABLED)
    boton_mostrar_pista.place_forget()
    boton_ocultar_pista.place(relx=0.47, rely=0.72, anchor=tk.CENTER)
    boton_nueva_pista.place(relx=0.53, rely=0.72, anchor=tk.CENTER)
    # Mostrar la ventana de respuesta
    respuesta_texto.place(relx=0.51, rely=0.56, anchor=tk.CENTER)

# Funcion accionada por el boton "Ocultar Pista", oculta la pista pedida por el usuario   
def ocultar_pista():
    # Ocultar la ventana de respuesta
    respuesta_texto.place_forget()
    # Ocultar el botón "Ocultar Historial" y mostrar el botón "Mostrar Historial"
    boton_ocultar_pista.place_forget()
    boton_mostrar_pista.place()

# Funcion para pedir una nueva pista
def nueva_pista():
    respuesta_texto.config(state=tk.NORMAL)
    global pista, response, historial, puntaje
    
    puntaje -= 20
    
    pista +=1
    if pista == 2:
        respuesta_texto.delete(1.0, tk.END) # Limpiamos el cuadro de pista
        boton_nueva_pista.place_forget()
        response = chatbot.model.generate_content(f'Dame una nueva pista igual de simple de: {palabra_random}')
        historial.append({"Role" : "IA", "Mensaje" : response.text})
        pista_texto = historial[1]
        respuesta_texto.insert(tk.END, f'{pista_texto["Mensaje"]}\n')
        respuesta_texto.config(state=tk.DISABLED)
        
# Función para reinciar el juego

def reiniciar_juego():
    # Restablecer las imagenes del progreso del juego
    if ahorcado2Label.winfo_ismapped():
        ahorcado2Label.place_forget()
    if ahorcado3Label.winfo_ismapped():   
        ahorcado3Label.place_forget()
    if ahorcado4Label.winfo_ismapped():
        ahorcado4Label.place_forget()
    if ahorcado5Label.winfo_ismapped():
        ahorcado5Label.place_forget()
    if ahorcado6Label.winfo_ismapped():
        ahorcado6Label.place_forget()
    # Reiniciar los valores del juego
    global pista, response, historial, puntaje, palabra_random, intentos, palabra, palabra_random_lista
    intentos = 0
    puntaje = 200
    pista = 0
    historial = []
    nueva_coleccion = random.choice(mongodb.colecciones)
    nueva_coleccionDB = mongodb.db[nueva_coleccion]
    nuevo_animal = nueva_coleccionDB.aggregate([{ "$sample": { "size": 1 } }]).next()
    nuevo_animal = nuevo_animal["Nombre"]
    palabra_randomN = nuevo_animal.upper() # Variable donde almacenamos la palabra random
    palabra_random = normalizar(palabra_randomN)
    palabra = ["_"] * len(palabra_random) # Lista del largo de la palabra aleatoria (sera mostrada en el progreso del juego)
    palabra_random_lista = list(palabra_random)
    progreso_puntaje.config(text=f'Puntaje Actual: {puntaje}')
    for i in range(len(palabra_random)):
                if palabra_random_lista[i] == " ":
                    palabra[i] = " "
    progreso_label.config(text= " ".join(palabra))                
    response = chatbot.model.generate_content(f'Generame una pista breve y no tan obvia sobre que animal es sin decirme su nombre {nuevo_animal}')
    historial.append({"Role" : "IA", "Mensaje" : response.text})

    # Elimina los elementos
    progreso_label.place_forget()
    respuesta_texto.place_forget()
    boton_enviar.place_forget()
    entradaAlimentacion.place_forget()
    boton_mostrar_pista.place_forget()
    boton_nueva_pista.place_forget()
    boton_ocultar_pista.place_forget()
    boton_reiniciar_juego.place_forget()
    

    
    # Limpiar el cuadro de texto
    respuesta_texto.config(state=tk.NORMAL)
    respuesta_texto.delete(1.0, tk.END)
    
    # Iniciamos nuevamente el juego
    ventana.after(200, iniciar_juego)
    

def salir():
    ventana.quit()
    
def cerrar_sesion():
    progreso_label.place_forget()
    respuesta_texto.place_forget()
    boton_enviar.place_forget()
    entradaAlimentacion.place_forget()
    boton_mostrar_pista.place_forget()
    boton_nueva_pista.place_forget()
    boton_ocultar_pista.place_forget()
    boton_reiniciar_juego.place_forget()
    HANGMANlabel.place_forget()
    ahorcado1Label.place_forget()
    progreso_puntaje.place_forget()
    ventana.after(500, inicio)

ventana = tk.Tk()
ventana.geometry("1280x960")
ventana.configure(background="#1e396b")
ventana.after(1000, inicio)
tk.Wm.wm_title(ventana, "HANGMAN - DevGroup")

# Crear la barra de menú
barra_menus = tk.Menu(ventana)
# Crear un menú de archivo
menu_archivo = tk.Menu(barra_menus, tearoff=0)
# Sub-menú de Usuario
menu_usuario = tk.Menu(menu_archivo, tearoff=0)
# Añadir opciones al submenú de Usuario
menu_usuario.add_command(label="Cambiar Contraseña", font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_usuario.add_command(label="Ver Puntaje", font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_usuario.add_separator()
menu_usuario.add_command(label="Cerrar Sesión", command=cerrar_sesion, font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_archivo.configure(background="#1e396b", activebackground="#1e396b")
menu_archivo.add_cascade(menu=menu_usuario,label="Usuario", font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_archivo.add_command(label="Clasificación", font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", font=("Arial", 9, "bold"), command=salir, background="#1e396b", foreground="#f6f6f6")
# Agregar el menú de archivo a la barra de menú
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)

def mostrar_acerca_de():
    acerca_de = tk.Toplevel()
    acerca_de.geometry("800x800-250+0")
    acerca_de.resizable(False, False)
    acerca_de.title("Acerca de")
    acerca_de.configure(background="#1e396b")

    acerca_de_portada = tk.Label(acerca_de, image=portadaIMG, bd=0)
    acerca_de_portada.pack()
    etiquetaTitulo = tk.Label(acerca_de, 
    text="Desafía tu ingenio con este emocionante juego de adivinanzas de palabras",
    bg="#1e396b", fg="#f6f6f6", font=("Calibri", 15, "bold")
    )
    etiquetaTitulo.place(relx=0.13, rely=0.2)

    etiqueta = tk.Label(acerca_de, 
    text="      Hangman es un juego de adivinanzas de palabras diseñado para desafiar y entretener a jugadores de todas las edades."
    " El objetivo es adivinar el\nnombre de un animal aleatorio seleccionado por el juego. Con múltiples niveles de dificultad, Hangman ofrece una experiencia desafiante y \n"
    "gratificante para los aficionados a los juegos de palabras.\n  - Características Destacadas:\n     Sistema"
    " de Puntaje Dinámico:\n         Los jugadores comienzan con un puntaje inicial de 200, el cual varía según "
    "sus acciones durante el juego. Cada intento fallido por adivinar la \npalabra resta 20 puntos, mientras que" 
    " solicitar pistas también reduce el puntaje en la misma cantidad. Por otro lado, adivinar la palabra sin pedir" 
    "\npistas aumenta el puntaje en 200 puntos. Este sistema de puntaje añade una capa adicional de estrategia y "
    "recompensa a la experiencia de juego.\n     Interfaz Intuitiva:\n         Hangman cuenta con una interfaz fácil"
    " de usar que permite a los jugadores navegar sin esfuerzo por el juego y disfrutar de una experiencia\n fluida"
    " y envolvente.\n Objetivo del Juego:\n    El objetivo principal de Hangman es adivinar correctamente el nombre del "
    "animal seleccionado, utilizando las letras disponibles y evitando los""\n errores para mantener el puntaje lo más "
    "alto posible.\n Los jugadores pueden poner a prueba su vocabulario, agudizar su pensamiento estratégico y disfrutar"
    " de horas de diversión desafiante mientras\n intentan alcanzar la cima de la clasificación.\n    ¡Únete a la "
    "emocionante aventura de Hangman y demuestra tu habilidad para descifrar palabras en este emocionante juego "
    "de adivinanzas \nde palabras!",
    bg="#1e396b", fg="#f6f6f6", justify="left", font=("Calibri", 10, "bold")
    )
    etiqueta.place(rely=0.5)

def creditos():
    creditos = tk.Toplevel()
    creditos.geometry("200x200-500-250")
    creditos.title("Creditos")
    creditos.resizable(False,False)
    creditos.configure(background="#1e396b")

    etiqueta = tk.Label(creditos, text="Desarrollado por:\n Dev-Group \n - Marcos Martos \n - Enzo Balderrama \n - Gabriel Gonzalez \n - Angelo Vellar \n - Santiago Peñafiel \n - Alejandro Perez \n - Joaquin Espósito \n - Bruno Olivera", bg="#1e396b", fg="#f6f6f6")
    etiqueta.pack(padx=20, pady=20)
# Crear un menú de ayuda
menu_ayuda = tk.Menu(barra_menus, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", font=("Arial", 9, "bold"), command= mostrar_acerca_de, background="#1e396b", foreground="#f6f6f6")
menu_ayuda.add_command(label="Creditos", font=("Arial", 9, "bold"), command= creditos, background="#1e396b", foreground="#f6f6f6")

# Agregar el menú de ayuda a la barra de menú
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

# Configurar la ventana principal para usar la barra de menú
ventana.config(menu=barra_menus)

portada = Image.open("Images/HANGMAN.jpeg")
portada = portada.resize((800, 800), Image.LANCZOS)
portadaIMG = ImageTk.PhotoImage(portada)
portadaLabel = tk.Label(ventana, image=portadaIMG, bd=0)
HANGMAN = Image.open("Images/HANGMANlabel.jpeg")
HANGMAN = HANGMAN.resize((250, 100), Image.LANCZOS)
HANGMANimg = ImageTk.PhotoImage(HANGMAN)
HANGMANlabel = tk.Label(ventana, image=HANGMANimg, bd= 0)
ahorcado1 = Image.open("Images/ahorcado1.jpg")
ahorcado1img = ImageTk.PhotoImage(ahorcado1)
ahorcado1Label = tk.Label(ventana, image=ahorcado1img, bd=0)
ahorcado2 = Image.open("Images/ahorcado2.jpg")
ahorcado2img = ImageTk.PhotoImage(ahorcado2)
ahorcado2Label = tk.Label(ventana, image=ahorcado2img, bd=0)
ahorcado3 = Image.open("Images/ahorcado3.jpg")
ahorcado3img = ImageTk.PhotoImage(ahorcado3)
ahorcado3Label = tk.Label(ventana, image=ahorcado3img, bd=0)
ahorcado4 = Image.open("Images/ahorcado4.jpg")
ahorcado4img = ImageTk.PhotoImage(ahorcado4)
ahorcado4Label = tk.Label(ventana, image=ahorcado4img, bd=0)
ahorcado5 = Image.open("Images/ahorcado5.jpg")
ahorcado5img = ImageTk.PhotoImage(ahorcado5)
ahorcado5Label = tk.Label(ventana, image=ahorcado5img, bd=0)
ahorcado6 = Image.open("Images/ahorcado6.jpg")
ahorcado6img = ImageTk.PhotoImage(ahorcado6)
ahorcado6Label = tk.Label(ventana, image=ahorcado6img, bd=0)


#Cargando imagenes de botones
boton_registroIMG = Image.open("Images/BotonRegistro.png")
boton_registroIMG = ImageTk.PhotoImage(boton_registroIMG)
boton_loginIMG = Image.open("Images/BotonIniciarSesion.png")
boton_loginIMG = ImageTk.PhotoImage(boton_loginIMG)
boton_salirIMG = Image.open("Images/BotonSalir.png")
boton_salirIMG = ImageTk.PhotoImage(boton_salirIMG)
boton_clasificacionIMG = Image.open("Images/BotonClasificacion.png")
boton_clasificacionIMG = ImageTk.PhotoImage(boton_clasificacionIMG)
boton_iniciarsesionIMG = Image.open("Images/BotonIniciarSesionMini.png")
boton_iniciarsesionIMG = ImageTk.PhotoImage(boton_iniciarsesionIMG)
boton_registarIMG = Image.open("Images/BotonRegistroMini.png")
boton_registarIMG = ImageTk.PhotoImage(boton_registarIMG)
boton_volverIMG = Image.open("Images/BotonVolver.png")
boton_volverIMG = ImageTk.PhotoImage(boton_volverIMG)
boton_reglasIMG = Image.open("Images/BotonReglas.png")
boton_reglasIMG = ImageTk.PhotoImage(boton_reglasIMG)
usuario = Image.open("Images/usuario.png")
usuarioIMG = ImageTk.PhotoImage(usuario)
contrasena = Image.open("Images/contraseña.png")
contrasenaIMG = ImageTk.PhotoImage(contrasena)

# Botones
boton_reiniciar_juego = tk.Button(ventana, text="Reiniciar", command=reiniciar_juego, bg="#022140", fg="#f6f6f6")
boton_mostrar_pista = tk.Button(ventana, text="Pedir pista", command=mostrar_pista, bg="#022140", fg="#f6f6f6")
boton_ocultar_pista = tk.Button(ventana, text="Ocultar pista", command=ocultar_pista, bg="#022140", fg="#f6f6f6")
boton_nueva_pista = tk.Button(ventana, text="Nueva pista", command=nueva_pista, bg="#022140", fg="#f6f6f6")
boton_registrar = tk.Button(ventana, image=boton_registarIMG, command=crear_usuario, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_iniciar = tk.Button(ventana, image=boton_loginIMG, bg="#1e396b", activebackground="#1e396b", command=login, bd=0)
boton_registro = tk.Button(ventana, image=boton_registroIMG, bg="#1e396b", activebackground="#1e396b", command=registro, bd=0)
boton_clasificacion = tk.Button(ventana, image=boton_clasificacionIMG, bg="#1e396b", activebackground="#1e396b", bd=0)
boton_salir = tk.Button(ventana, image=boton_salirIMG, bg="#1e396b", activebackground="#1e396b", command=salir, bd=0)
boton_enviar = tk.Button(ventana, text="Enviar", padx=10, pady=5, command=entrada, bg="#022140", fg="#f6f6f6")
boton_iniciarsesion = tk.Button(ventana, image=boton_iniciarsesionIMG, command=comprobar_usuarios, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_volver = tk.Button(ventana, image= boton_volverIMG, command=inicio, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_reglas = tk.Button(ventana, image=boton_reglasIMG, command=mostrar_acerca_de, activebackground="#1e396b", bg="#1e396b", bd=0)

# Etiquetas
progreso_label = tk.Label(ventana, text= " ".join(palabra), font=("Verdana", 16), bg="#1e396b", fg="#f6f6f6")
progreso_puntaje = tk.Label(ventana, text= f'Puntaje Actual: {puntaje}', font=("Verdana", 14), bg="#1e396b", fg="#f6f6f6")
label_bienvenida = tk.Label(ventana, text = "", bg="#1e396b", fg="#f6f6f6")
label_login = tk.Label(ventana, image=usuarioIMG, bg="#1e396b", fg="#f6f6f6")
label_password = tk.Label(ventana, image=contrasenaIMG, bg="#1e396b", fg="#f6f6f6")

# Entradas de texto
entradaAlimentacion = tk.Text(ventana, width= 40, height=2, bg="#022140", fg="#f6f6f6") # Configuramos el tamaño de la ventana de alimentación
entradaLogin = tk.Text(ventana, width=11, height=1,bg="#022140", fg="#f6f6f6", font=("Verdana", 14))
entradaPassword = tk.Entry(ventana, width=11, bg="#022140", fg="#f6f6f6", font=("Verdana", 14), show="*")
respuesta_texto = tk.Text(ventana, width=40, height=10, bg="#022140", fg="#f6f6f6", bd=0)

ventana.mainloop()