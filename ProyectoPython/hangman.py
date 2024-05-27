import unicodedata
import mongodb
import googleapi as chatbot
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Funcion para el login
def login():
    boton_iniciar.place_forget()
    boton_registro.place_forget()
    label_login.place(relx=0.474, rely=0.395, anchor=tk.CENTER)
    entradaLogin.place(relx=0.536, rely=0.395, anchor=tk.CENTER)
    label_password.place(relx=0.475, rely=0.425, anchor=tk.CENTER)
    entradaPassword.place(relx=0.536, rely=0.425, anchor=tk.CENTER)
    boton_iniciarsesion.place(relx=0.51, rely=0.5, anchor=tk.CENTER)
    

def registro():
    boton_iniciar.place_forget()
    boton_registro.place_forget()
    label_login.place(relx=0.474, rely=0.395, anchor=tk.CENTER)
    entradaLogin.place(relx=0.536, rely=0.395, anchor=tk.CENTER)
    label_password.place(relx=0.475, rely=0.425, anchor=tk.CENTER)
    entradaPassword.place(relx=0.536, rely=0.425, anchor=tk.CENTER)
    boton_iniciarsesion.place(relx=0.51, rely=0.5, anchor=tk.CENTER)

def crear_usuario():
    usuario = entradaLogin.get("1.0","end-1c").strip()
    password = entradaPassword.get("1.0", "end-1c").strip()
    comprobar = tk.Label(ventana, text="", font=("Arial", 9, "bold"), bg="#1e396b", fg="#f6f6f6")
    try:
        nuevo_usuario = mongodb.listaUsuarios.insert_one({"Nombre" : usuario,"Contraseña" : password})
        if nuevo_usuario.inserted_id:
            entradaLogin.place_forget()
            label_password.place_forget()
            entradaPassword.place_forget()
            label_login.place_forget()
            boton_registrar.place_forget()
            comprobar.config(text="Usuario creado correctamente")
            comprobar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    except:
        comprobar.config(text="ERROR. No se pudo crear el usuario.")
        comprobar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



def comprobar_usuarios():
    usuario = entradaLogin.get("1.0","end-1c").strip()
    password = entradaPassword.get().strip()
    if mongodb.dbUsers.listaUsuarios.find_one({"Nombre" : usuario, "Contraseña" : password}):
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
        label_bienvenida.place(relx=0.5,rely=0.4, anchor=tk.CENTER) 
    
# Funcion para normalizar las cadenas de texto
def normalizar (cadena):
    return " ".join(
        c for c in unicodedata.normalize("NFD", cadena)
        if unicodedata.category(c) != "Mn"
    )


response = chatbot.model.generate_content(f'Generame una pista breve y no tan obvia sobre que animal es sin decirme su nombre {mongodb.respuesta}')
historial = []
historial.append(response.text)
palabra_randomN = mongodb.respuesta.upper()
palabra_random = normalizar(palabra_randomN)
palabra = ["_"] * len(palabra_random)
palabra_random_lista = list(palabra_random)
intentos = 0
for i in range(len(palabra_random)):
                if palabra_random_lista[i] == " ":
                    palabra[i] = " "
# ALIMENTACION
def entrada():
    pregunta =  normalizar(entradaAlimentacion.get("1.0","end-1c").upper())
    global intentos
    
    # Lógica del juego
    
    if len(pregunta) == 1:
        if pregunta in palabra_random:
            for i in range(len(palabra_random)):
                if palabra_random_lista[i] == pregunta:
                    palabra[i] = pregunta
            actualizar_progreso(palabra)       
        else:
            intentos +=1
    else:
        if pregunta == palabra_random:
            progreso_label.config(text=f"¡Ganaste! \n La palabra era: {palabra_random}")
        else:
            intentos += 1
    
    # Actualizar estado de intentos
    if intentos == 1:
                ahorcado1Label.destroy()
                ahorcado2Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 2:
        ahorcado2Label.destroy()
        ahorcado3Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 3:
        ahorcado3Label.destroy()
        ahorcado4Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 4:
        ahorcado4Label.destroy()
        ahorcado5Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    elif intentos == 5:
        ahorcado5Label.destroy()
        ahorcado6Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
        
                    
    # Chequear si el juego ha terminado
    if "".join(palabra) == palabra_random:
            progreso_label.config(text=f"¡Ganaste! \n La palabra era: {palabra_random}")
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
    ahorcado1Label.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
    HANGMANlabel.place(relx= 0.51, rely=0.15, anchor=tk.CENTER)

    # Ocultar el botón "Iniciar"
    portadaLabel.destroy()
    label_bienvenida.destroy()
    boton_iniciar.place_forget()
    
def mostrar_pista():
    # Mostrar el historial en la ventana de respuesta
    for mensaje in historial:
        respuesta_texto.insert(tk.END, f"{mensaje}\n")
    # Deshabilitar el widget para hacerlo de solo lectura
    respuesta_texto.config(state=tk.DISABLED)
    boton_mostrar_pista.place_forget()
    boton_ocultar_pista.place(relx=0.51, rely=0.72, anchor=tk.CENTER)
    # Mostrar la ventana de respuesta
    respuesta_texto.place(relx=0.51, rely=0.56, anchor=tk.CENTER)
    
def ocultar_pista():
    # Ocultar la ventana de respuesta
    respuesta_texto.place_forget()
    # Ocultar el botón "Ocultar Historial" y mostrar el botón "Mostrar Historial"
    boton_ocultar_pista.place_forget()
    boton_mostrar_pista.place()
    
def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.geometry("1280x960")
ventana.configure(background="#1e396b")

tk.Wm.wm_title(ventana, "HANGMAN - DevGroup")

# Crear la barra de menú
barra_menus = tk.Menu(ventana)

# Crear un menú de archivo
menu_archivo = tk.Menu(barra_menus, tearoff=0)
menu_archivo.add_command(label="Usuario")
menu_archivo.add_command(label="Clasificación")
menu_archivo.add_command(label="Dificultad")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Agregar el menú de archivo a la barra de menú
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)

def mostrar_acerca_de():
    acerca_de = tk.Toplevel()
    acerca_de.geometry("200x200-500-250")
    acerca_de.title("Acerca de")
    acerca_de.resizable(False,False)
    acerca_de.configure(background="#1e396b")

    etiqueta = tk.Label(acerca_de, text="Desarrollado por:\n Dev-Group \n - Marcos Martos \n - Enzo Balderrama \n - Gabriel Gonzalez \n - Angelo Vellar \n - Santiago Peñafiel \n - Alejandro Perez \n - Joaquin Espósito \n - Bruno Olivera", 
                        bg="#1e396b", fg="#f6f6f6")
    etiqueta.pack(padx=20, pady=20)

    boton_cerrar = tk.Button(acerca_de, text="Cerrar", command=acerca_de.destroy, bg="#f6f6f6", fg="#1e396b")
    boton_cerrar.pack(pady=(0, 20))
# Crear un menú de ayuda
menu_ayuda = tk.Menu(barra_menus, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command= mostrar_acerca_de, background="#1e396b", foreground="#f6f6f6")

# Agregar el menú de ayuda a la barra de menú
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

# Configurar la ventana principal para usar la barra de menú
ventana.config(menu=barra_menus)

portada = Image.open("Images/HANGMAN.jpeg")
portada = portada.resize((800, 800), Image.LANCZOS)
portadaIMG = ImageTk.PhotoImage(portada)
portadaLabel = tk.Label(ventana, image=portadaIMG, bd=0)
portadaLabel.pack()
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


# Botones
# Configurar el botón para mostrar el historial
boton_mostrar_pista = tk.Button(ventana, text="Pedir pista", command=mostrar_pista, bg="#022140", fg="#f6f6f6")
# Configurar el botón para ocultar el historial
boton_ocultar_pista = tk.Button(ventana, text="Ocultar pista", command=ocultar_pista, bg="#022140", fg="#f6f6f6")
boton_registrar = tk.Button(ventana, text="Registrar", command=crear_usuario, font=("Arial", 10, "bold"), fg="#f6f6f6", bg="#000323", bd=0)
boton_iniciar = tk.Button(ventana, text="INICIAR SESION", command=login, font=("Arial", 10, "bold"), fg="#f6f6f6", bg="#000323", bd=0)
boton_iniciar.place(relx=0.5, rely=0.32, anchor=tk.CENTER)
boton_registro = tk.Button(ventana, text="     REGISTRO    ", command=registro, font=("Arial", 10, "bold"), fg="#f6f6f6", bg="#000323", bd=0)
boton_registro.place(relx=0.501, rely=0.29, anchor=tk.CENTER)
boton_enviar = tk.Button(ventana, text="Enviar", padx=10, pady=5, command=entrada)
boton_iniciarsesion = tk.Button(ventana, text="Iniciar Sesión", command=comprobar_usuarios, font=("Arial", 10, "bold"), fg="#f6f6f6", bg="#000323", bd=0)

# Etiquetas
progreso_label = tk.Label(ventana, text= " ".join(palabra), font=("Arial", 16), bg="#1e396b", fg="#f6f6f6")
label_bienvenida = tk.Label(ventana, text = "", bg="#1e396b", fg="#f6f6f6")
label_login = tk.Label(ventana, text="Usuario:        ", font=("Arial", 9, "bold"), bg="#1e396b", fg="#f6f6f6")
label_password = tk.Label(ventana, text="Contraseña: ", font=("Arial", 9, "bold"), bg="#1e396b", fg="#f6f6f6")


 
entradaAlimentacion = tk.Text(ventana, width= 40, height=3, bg="#022140", fg="#f6f6f6") # Configuramos el tamaño de la ventana de alimentación
entradaLogin = tk.Text(ventana, width=11, height=1,bg="#022140", fg="#f6f6f6", font=("Arial", 10, "bold"))
entradaPassword = tk.Entry(ventana, width=11,bg="#022140", fg="#f6f6f6", font=("Arial", 10, "bold"), show="*")



respuesta_texto = tk.Text(ventana, width=40, height=10, bg="#022140", fg="#f6f6f6", bd=0)
ventana.mainloop()


# PARA HACER
# 
# 
# 
#       O la cabeza está siempre
#      /|\
#      /\
#
# 
# 
# agregar opcion de reiniciar
# agregar un menú, elegir usuario, mostrar el ranking, creditos, reiniciar y seleccionar dificultad.
# hacer un login de usuario con una base de datos que contenga nombre de usuario y puntuación.

    
# hacer una clasificacion de los jugadores con mas puntaje.
