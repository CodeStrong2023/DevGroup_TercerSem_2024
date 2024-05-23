import pymongo
import mongodb
import googleapi as chatbot
import tkinter as tk
import google.generativeai as genai
from PIL import Image, ImageTk

response = chatbot.model.generate_content(f'Generame una pista breve y no tan obvia sobre que animal es sin decirme su nombre {mongodb.respuesta}')
historial = []
historial.append(response.text)
palabra_random = mongodb.respuesta.upper()
palabra = ["_"] * len(palabra_random)
palabra_random_lista = list(palabra_random)
intentos = 0

# ALIMENTACION
def entrada():
    pregunta =  entradaAlimentacion.get("1.0","end-1c").upper()
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
            progreso_label.config(text="¡Ganaste!")
        else:
            intentos += 1
                    
    # Chequear si el juego ha terminado
    if "".join(palabra) == palabra_random:
            progreso_label.config(text="¡Ganaste!")
    elif intentos >= 6:
            progreso_label.config(text=f"Perdiste. La palabra era: {palabra_random}")

    entradaAlimentacion.delete(1.0, tk.END) # BORRA LOS TEXTOS INGRESADOS

# Crear la función para actualizar el label de progreso
def actualizar_progreso(palabra):
    progreso_label.config(text=" ".join(palabra))
    
# Funcion para mostrar el contenido del juego
def iniciar_juego():
    # Mostrar todos los widgets del juego
    progreso_label.pack(side=tk.TOP, pady=10)
    boton_enviar.pack(side=tk.BOTTOM, pady=10)
    entradaAlimentacion.pack(side=tk.BOTTOM, pady=10)
    boton_mostrar_pista.pack(side=tk.BOTTOM, pady=10)
    # Ocultar el botón "Iniciar"
    portadaLabel.pack_forget()
    boton_iniciar.place_forget()
    
def mostrar_pista():
    # Mostrar el historial en la ventana de respuesta
    for mensaje in historial:
        respuesta_texto.insert(tk.END, f"{mensaje}\n")
    # Deshabilitar el widget para hacerlo de solo lectura
    respuesta_texto.config(state=tk.DISABLED)
    boton_mostrar_pista.pack_forget()
    boton_ocultar_pista.pack(side=tk.BOTTOM, pady=10)
    # Mostrar la ventana de respuesta
    respuesta_texto.pack(side=tk.BOTTOM, pady=10)
    
def ocultar_pista():
    # Ocultar la ventana de respuesta
    respuesta_texto.pack_forget()
    # Ocultar el botón "Ocultar Historial" y mostrar el botón "Mostrar Historial"
    boton_ocultar_pista.pack_forget()
    boton_mostrar_pista.pack(side=tk.BOTTOM, pady=10)

ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(background="#022140")

tk.Wm.wm_title(ventana, "HANGMAN - DevGroup")

portada = Image.open("Images/HANGMAN.jpeg")
portada = portada.resize((800, 800), Image.LANCZOS)
portadaIMG = ImageTk.PhotoImage(portada)
portadaLabel = tk.Label(ventana, image=portadaIMG, bd=0)
portadaLabel.pack()

# Crear el botón "Iniciar" que mostrará los demás widgets
boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar_juego, font=("Arial", 14, "bold"), bg="#f6f6f6", fg="#000323", bd=0)
boton_iniciar.place(relx=0.51, rely=0.93, anchor=tk.CENTER)

# Crear el label para mostrar el progreso del juego
progreso_label = tk.Label(ventana, text= palabra, font=("Arial", 16), bg="#022140", fg="#f6f6f6")


boton_enviar = tk.Button(ventana, text="Enviar", padx=10, pady=5, command=entrada) 
entradaAlimentacion = tk.Text(ventana, width= 40, height=3) # Configuramos el tamaño de la ventana de alimentación

# Configurar el botón para mostrar el historial
boton_mostrar_pista = tk.Button(ventana, text="Pedir pista", command=mostrar_pista, bg="#022140", fg="#f6f6f6")
# Configurar el botón para ocultar el historial
boton_ocultar_pista = tk.Button(ventana, text="Ocultar pista", command=ocultar_pista, bg="#022140", fg="#f6f6f6")

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
# agregar lógica para que no pida los espacios en blanco, y para que a la entrada 
# la tome sin los espacios en blanco y compare con la palabra_random sin los espacios en blanco.
# agregar un menú, elegir usuario, mostrar el ranking, creditos, reiniciar y seleccionar dificultad.
# modificar la función "entrada" para que acepte la palabra completa
# hacer un login de usuario con una base de datos que contenga nombre de usuario y puntuación.
# hacer una clasificacion de los jugadores con mas puntaje.
# mostrar un teclado en pantalla.
