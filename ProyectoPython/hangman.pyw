import random
from time import sleep
import unicodedata
import mongodb
import googleapi as chatbot
import tkinter as tk
import Images.imagenes as imagenes


# Función para la ventana principal del juego
def inicio():
    for widget in ventana.winfo_children(): # Ocultar todos los widgets de la ventana
        widget.place_forget()
        widget.grid_forget()
        widget.pack_forget()
    if entradaPassword.get():
        entradaPassword.delete(0, tk.END)
    if entradaLogin.get(1.0, tk.END).strip():
        entradaLogin.delete(1.0, tk.END)
    global usuarioBool 
    usuarioBool = False
    portadaLabel.pack(side="left")
    boton_iniciar.place(relx=0.81, rely=0.29, anchor=tk.CENTER)
    boton_registro.place(relx=0.81, rely=0.2, anchor=tk.CENTER)
    boton_clasificacion.place(relx=0.81, rely=0.38, anchor=tk.CENTER)
    boton_salir.place(relx=0.81, rely = 0.8, anchor=tk.CENTER)
    boton_reglas.place(relx=0.81, rely=0.47, anchor=tk.CENTER)
    


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
    comprobar = tk.Label(ventana, font=("Verdana", 16, "bold"), bg="#1e396b", fg="#f6f6f6")

    try:
        
        if usuario != "":
            # Verifica si el usuario ya existe
            usuario_existente = mongodb.listaUsuarios.find_one({"Nombre": usuario.upper()})
            if usuario_existente:
                if comprobar.winfo_ismapped():
                    comprobar.place_forget()
                comprobar.config(image=img["usuarioExistenteIMG"])
                comprobar.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
                return
                
        
            # Inserta un nuevo usuario si no existe
            nuevo_usuario = mongodb.listaUsuarios.insert_one({"Nombre" : usuario.upper(),"Contraseña" : password, "Puntaje" : 0, "Palabras Acertadas" : 0})
            if nuevo_usuario.inserted_id:
                comprobar.config(text=f"USUARIO {usuario} CREADO CORRECTAMENTE")
                comprobar.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
        else:
            if comprobar.winfo_ismapped():
                comprobar.place_forget()
            comprobar.config(image=img["usuarioVacioIMG"])
            comprobar.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
            return
    except:
        comprobar.config(text="ERROR. No se pudo crear el usuario.")
        comprobar.place(relx=0.8, rely=0.3, anchor=tk.CENTER)

usuario = "" # Variable global donde guardaremos el usuario que se ingese por teclado
usuarioDoc = [] # Aqui es donde luego guardaremos el documento de dicho usuario
usuarioBool = False # Con esta variable detectamos si el usuario está logeado o no

# Funcion para comprobar si el usuario ingresado existe, en caso True, se logea dicho usuario
def comprobar_usuarios():
    global usuario
    global usuarioDoc, usuarioBool
    # Entradas para el nombre y contraseña del usuario
    usuario = entradaLogin.get("1.0","end-1c").strip()
    password = entradaPassword.get().strip()
    
    # Comprobamos si el usuario existe
    if mongodb.dbUsers.listaUsuarios.find_one({"Nombre" : usuario.upper(), "Contraseña" : password}):
        usuarioDoc = mongodb.listaUsuarios.find_one({"Nombre" : usuario.upper()})
        usuarioBool = True
        entradaLogin.place_forget()
        label_password.place_forget()
        entradaPassword.place_forget()
        label_login.place_forget()
        boton_iniciarsesion.place_forget()
        label_bienvenida.config(text=f"Bienvenido/a {usuario}", font=("Arial", 14, "bold"))
        label_bienvenida.place(relx=0.8,rely=0.4, anchor=tk.CENTER)
        boton_volver.place_forget()
        ventana.after(2000, iniciar_juego)
    else:
        label_bienvenida.config(text="USUARIO O CONTRASEÑA INCORRECTOS", font=("Arial", 14, "bold"))
        label_bienvenida.place(relx=0.8,rely=0.3, anchor=tk.CENTER)

    
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
            usuarioDoc = mongodb.listaUsuarios.find_one({"_id" : UsuarioID})
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
            usuarioDoc = mongodb.listaUsuarios.find_one({"_id" : UsuarioID})
    elif intentos >= 6:
            progreso_label.config(text=f"Perdiste. La palabra era: {palabra_random}")

    entradaAlimentacion.delete(1.0, tk.END) # BORRA LOS TEXTOS INGRESADOS




# Crear la función para actualizar el label de progreso
def actualizar_progreso(palabra):
    progreso_label.config(text=" ".join(palabra))

    
# Funcion para mostrar el contenido del juego
def iniciar_juego():
    for widget in ventana.winfo_children(): # Ocultar todos los widgets de la ventana
        widget.place_forget()
        widget.grid_forget()
        widget.pack_forget()
    # Mostrar todos los widgets del juego
    progreso_label.place(relx=0.51, rely=0.25, anchor=tk.CENTER)
    boton_enviar.place(relx=0.51, rely=0.93, anchor=tk.CENTER)
    entradaAlimentacion.place(relx=0.51, rely=0.8, anchor=tk.CENTER)
    boton_mostrar_pista.place(relx=0.51, rely=0.72, anchor=tk.CENTER)
    boton_reiniciar_juego.place(relx=0.71, rely=0.93, anchor=tk.CENTER)
    ahorcado1Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    progreso_puntaje.place(relx=0.51, rely=0.85, anchor=tk.CENTER)
    HANGMANlabel.place(relx= 0.51, rely=0.15, anchor=tk.CENTER)
    
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
    while True:
        try:
            if pista == 2:
                respuesta_texto.delete(1.0, tk.END) # Limpiamos el cuadro de pista
                response = chatbot.model.generate_content(f'Dame una nueva pista igual de simple de: {palabra_random}')
                historial.append({"Role" : "IA", "Mensaje" : response.text})
                pista_texto = historial[1]
                boton_nueva_pista.place_forget()
                respuesta_texto.insert(tk.END, f'{pista_texto["Mensaje"]}\n')
                respuesta_texto.config(state=tk.DISABLED)
            break
        except:
            sleep(0.1)
        
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
    while True:
        try:                
            response = chatbot.model.generate_content(f'Generame una pista breve y no tan obvia sobre que animal es sin decirme su nombre {nuevo_animal}')
            historial.append({"Role" : "IA", "Mensaje" : response.text})
            break
        except:
            sleep(0.1)
    entradaAlimentacion.delete(1.0, tk.END)
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
    

def clasificacion():
    portadaLabel.place(anchor=tk.CENTER)
    for widget in ventana.winfo_children(): # Ocultar todos los widgets de la ventana
        widget.place_forget()
        widget.grid_forget()
        widget.pack_forget()
    top_users = mongodb.listaUsuarios.find().sort("Puntaje", -1).limit(10)
    # Inicializar listas para nombres y puntajes
    top_users_names = []
    top_users_points = []
    top_users_words = []

    # Llenar las listas con los datos obtenidos
    for user in top_users:
        top_users_names.append(user.get("Nombre", "NO SE HA DETECTADO JUGADOR"))
        top_users_points.append(user.get("Puntaje", 0))
        top_users_words.append(user.get("Palabras Acertadas", 0))

    # Rellenar las listas si tienen menos de 10 elementos
    while len(top_users_names) < 10:
        top_users_names.append("NO SE HA DETECTADO JUGADOR")
        top_users_points.append(0)
        top_users_words.append(0)

    # Verificar si hay nombres no detectados y asignar valores predeterminados
    for i in range(len(top_users_names)):
        if top_users_names[i] is None:
            top_users_names[i] = "NO SE HA DETECTADO JUGADOR"
        if top_users_points[i] is None:
            top_users_points[i] = 0
        if top_users_words[i] is None:
            top_users_words[i] = 0

    for i in range(1,11):
        if i - 11:
            etiqueta1 = tk.Label(ventana, image=img[f"nro{i}"], background="#1e396b", bd=0)
            etiqueta1.grid(row=i,column=0)
    for i in range(1,11):
        nombre1 = tk.Label(ventana, text=top_users_names[i-1], font=("Arial", 16, "bold"), background="#1e396b", foreground="#ffffff", bd=0, highlightbackground="#000323", highlightthickness=0.5)
        nombre1.grid(row=i,column=1, sticky="nsew")
        nombre2 = tk.Label(ventana, text=top_users_points[i-1], font=("Arial", 16, "bold"), background="#1e396b", foreground="#ffffff", bd=0, highlightbackground="#000323", highlightthickness=0.5)
        nombre2.grid(row=i,column=3, sticky="nsew")
        nombre3 = tk.Label(ventana, text=top_users_words[i-1], font=("Arial", 16, "bold"), background="#1e396b", foreground="#ffffff", bd=0, highlightbackground="#000323", highlightthickness=0.5)
        nombre3.grid(row=i,column=2, sticky="nsew")
    etiquetaNombre = tk.Label(ventana, background="#1e396b", image=img["nombre"], bd = 0)
    etiquetaPalabrasAcertadas = tk.Label(ventana, background="#1e396b", image=img["palabras_adivinadas"], bd=0)
    etiquetaPuntaje = tk.Label(ventana,background="#1e396b", image=img["puntaje"], bd=0)
    etiquetaNombre.grid(row=0, column=1)
    etiquetaPalabrasAcertadas.grid(row=0, column=2)
    etiquetaPuntaje.grid(row=0, column=3)
    boton_volver_clasificacion.grid(row=12,column=3)

def usuarioLogeado():
    if usuarioBool:
        iniciar_juego()
    else:
        inicio()

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

def actualizar_password(window, nuevapass):
    nueva_contrasena = nuevapass.get().strip()
    contrasena_actualizada = tk.Label(window, font=("Verdana", 12), bg="#1e396b", fg="#f6f6f6")
    if nueva_contrasena:
        contrasena_actualizada.config(image=img["contrasenaActualizadaIMG"])
        contrasena_actualizada.place(relx = 0.5, rely = 0.2, anchor = tk.CENTER)
        mongodb.listaUsuarios.update_one({"_id" : usuarioDoc["_id"]},  { "$set": {"Contraseña" : nueva_contrasena}})
    else:
        contrasena_actualizada.config(image=img["contrasenaVaciaIMG"])
        contrasena_actualizada.place(relx = 0.5, rely = 0.2, anchor = tk.CENTER)
       
def cambiar_password():
    cambiar_password = tk.Toplevel()
    cambiar_password.geometry("350x100-200-250")
    cambiar_password.resizable(False, False)
    cambiar_password.title("Cambiar Contraseña")
    cambiar_password.configure(background="#1e396b")
    entrada_Password = tk.Entry(cambiar_password, width=11, bg="#022140", fg="#f6f6f6", font=("Verdana", 14), show="*")
    labelpassword = tk.Label(cambiar_password, image=img["contrasenaIMG"], bg="#1e396b", fg="#f6f6f6")
    labeluser = tk.Label(cambiar_password,text="No existe ningun usuario.", bg="#022140", fg="#f6f6f6", font=("Verdana", 14))
    
    if usuarioBool:
        labelpassword.place(relx = 0.3, rely = 0.5, anchor = tk.CENTER)
        entrada_Password.place(relx = 0.7, rely = 0.5, anchor = tk.CENTER)
        boton_cambiar = tk.Button(cambiar_password, image=img["boton_aceptarIMG"], command=lambda: actualizar_password(cambiar_password, entrada_Password), bg="#1e396b", activebackground="#1e396b", bd=0)
        boton_cambiar.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)
    else:
        labeluser.pack(fill="both", expand=True)

def ver_puntaje():
    ver_puntos = tk.Toplevel()
    ver_puntos.geometry("350x140-250-250")
    ver_puntos.resizable(False, False)
    ver_puntos.title("Puntaje Historico")
    ver_puntos.configure(background="#1e396b")
    puntajeLabel = tk.Label(ver_puntos, image=img["puntaje_usuarioIMG"], bg="#1e396b", activebackground="#1e396b", bd=0)
    palabras_acertadas_label = tk.Label(ver_puntos, image=img["palabras_acertadasIMG"], bg="#1e396b", bd=0)
    usuario_inexistente = tk.Label(ver_puntos, text="No existe ningun usuario.".upper(), bg="#022140", fg="#f6f6f6", font=("Verdana", 14))
    
    if usuarioBool:
        puntajeLabel.pack(side="top", fill="x", pady=0.5)
        puntaje_actual = tk.Label(ver_puntos, text=usuarioDoc["Puntaje"], bg="#022140", fg="#f6f6f6", font=("Verdana", 14, "bold"))
        puntaje_actual.pack(side="top", fill="x", expand=True, pady=1)
        palabras_acertadas_label.pack(side="top", fill="x", pady=0.5)
        palabras_acertadas = tk.Label(ver_puntos, text=usuarioDoc["Palabras Acertadas"], bg="#022140", fg="#f6f6f6", font=("Verdana", 14, "bold"))
        palabras_acertadas.pack(side="bottom", fill="x", expand=True)
    else:
        usuario_inexistente.pack(fill="both", expand=True)
        
ventana = tk.Tk()
ventana.geometry("1280x960")
ventana.configure(background="#1e396b")
ventana.attributes("-fullscreen", True)
ventana.after(1000, inicio)
tk.Wm.wm_title(ventana, "HANGMAN - DevGroup")

img = imagenes.cargar_imagenes(ventana)
# Crear la barra de menú
barra_menus = tk.Menu(ventana)
# Crear un menú de archivo
menu_archivo = tk.Menu(barra_menus, tearoff=0)
# Sub-menú de Usuario
menu_usuario = tk.Menu(menu_archivo, tearoff=0)
# Añadir opciones al submenú de Usuario
menu_usuario.add_command(label="Cambiar Contraseña", command=cambiar_password, font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_usuario.add_command(label="Ver Puntaje", font=("Arial", 9, "bold"), command=ver_puntaje , background="#1e396b", foreground="#f6f6f6")
menu_usuario.add_separator()
menu_usuario.add_command(label="Cerrar Sesión", command=cerrar_sesion, font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_archivo.configure(background="#1e396b", activebackground="#1e396b")
menu_archivo.add_cascade(menu=menu_usuario,label="Usuario", font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
menu_archivo.add_command(label="Clasificación", command=clasificacion, font=("Arial", 9, "bold"), background="#1e396b", foreground="#f6f6f6")
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

    acerca_de_portada = tk.Label(acerca_de, image=img["portadaIMG"], bd=0)
    acerca_de_portada.pack(side="left", fill="both",expand=True)
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

# Botones
boton_reiniciar_juego = tk.Button(ventana, text="Reiniciar", command=reiniciar_juego, bg="#022140", fg="#f6f6f6")
boton_mostrar_pista = tk.Button(ventana, text="Pedir pista", command=mostrar_pista, bg="#022140", fg="#f6f6f6")
boton_ocultar_pista = tk.Button(ventana, text="Ocultar pista", command=ocultar_pista, bg="#022140", fg="#f6f6f6")
boton_nueva_pista = tk.Button(ventana, text="Nueva pista", command=nueva_pista, bg="#022140", fg="#f6f6f6")
boton_registrar = tk.Button(ventana, image=img["boton_registrarIMG"], command=crear_usuario, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_iniciar = tk.Button(ventana, image=img["boton_loginIMG"], bg="#1e396b", activebackground="#1e396b", command=login, bd=0)
boton_registro = tk.Button(ventana, image=img["boton_registroIMG"], bg="#1e396b", activebackground="#1e396b", command=registro, bd=0)
boton_clasificacion = tk.Button(ventana, command=clasificacion, image=img["boton_clasificacionIMG"], bg="#1e396b", activebackground="#1e396b", bd=0)
boton_salir = tk.Button(ventana, image=img["boton_salirIMG"], bg="#1e396b", activebackground="#1e396b", command=salir, bd=0)
boton_enviar = tk.Button(ventana, text="Enviar", padx=10, pady=5, command=entrada, bg="#022140", fg="#f6f6f6")
boton_iniciarsesion = tk.Button(ventana, image=img["boton_iniciarsesionIMG"], command=comprobar_usuarios, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_volver = tk.Button(ventana, image= img["boton_volverIMG"], command=inicio, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_volver_clasificacion = tk.Button(ventana, image= img["boton_volverIMG"], command=usuarioLogeado, activebackground="#1e396b", bg="#1e396b", bd=0)
boton_reglas = tk.Button(ventana, image= img["boton_reglasIMG"], command=mostrar_acerca_de, activebackground="#1e396b", bg="#1e396b", bd=0)

# Etiquetas
portadaLabel = tk.Label(ventana, image=img["portadaIMG"], bd=0)
HANGMANlabel = tk.Label(ventana, image=img["HANGMANimg"], bd= 0)
ahorcado1Label = tk.Label(ventana, image=img["ahorcado1img"], bd=0)
ahorcado2Label = tk.Label(ventana, image=img["ahorcado2img"], bd=0)
ahorcado3Label = tk.Label(ventana, image=img["ahorcado3img"], bd=0)
ahorcado4Label = tk.Label(ventana, image=img["ahorcado4img"], bd=0)
ahorcado5Label = tk.Label(ventana, image=img["ahorcado5img"], bd=0)
ahorcado6Label = tk.Label(ventana, image=img["ahorcado6img"], bd=0)
progreso_label = tk.Label(ventana, text= " ".join(palabra), font=("Verdana", 16), bg="#1e396b", fg="#f6f6f6")
progreso_puntaje = tk.Label(ventana, text= f'Puntaje Actual: {puntaje}', font=("Verdana", 14), bg="#1e396b", fg="#f6f6f6")
label_bienvenida = tk.Label(ventana, text = "", bg="#1e396b", fg="#f6f6f6")
label_login = tk.Label(ventana, image=img["usuarioIMG"], bg="#1e396b", fg="#f6f6f6")
label_password = tk.Label(ventana, image=img["contrasenaIMG"], bg="#1e396b", fg="#f6f6f6")

# Entradas de texto
entradaAlimentacion = tk.Text(ventana, width= 40, height=2, bg="#022140", fg="#f6f6f6") # Configuramos el tamaño de la ventana de alimentación
entradaLogin = tk.Text(ventana, width=11, height=1,bg="#022140", fg="#f6f6f6", font=("Verdana", 14))
entradaPassword = tk.Entry(ventana, width=11, bg="#022140", fg="#f6f6f6", font=("Verdana", 14), show="*")
respuesta_texto = tk.Text(ventana, width=40, height=10, bg="#022140", fg="#f6f6f6", bd=0)

ventana.mainloop()