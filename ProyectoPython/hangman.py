import pymongo
import mongodb
import googleapi as chatbot
import tkinter as tk
import google.generativeai as genai

response = chatbot.model.generate_content(f'Generame una pista breve y no tan obvia sobre que animal es sin decirme su nombre {pruebaMongo.respuesta}')
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
    
    if pregunta in palabra_random:
        for i in range(len(palabra_random)):
            if palabra_random_lista[i] == pregunta:
                palabra[i] = pregunta
        actualizar_progreso(palabra)       
    else:
        intentos +=1
                    
            # Chequear si el juego ha terminado
    if "".join(palabra) == palabra_random:
            progreso_label.config(text="¡Ganaste!")
    elif intentos >= 6:
            progreso_label.config(text=f"Perdiste. La palabra era: {palabra_random}")

#    historial.append({"Role" : "User", "content" : pregunta})
#    response = chatbot.model.generate_content(pregunta)
#    historial.append({"Role" : "Hangman", "content" : response.text})

    entradaAlimentacion.delete(1.0, tk.END) # BORRA LOS TEXTOS INGRESADOS

# Crear la función para actualizar el label de progreso
def actualizar_progreso(palabra):
    progreso_label.config(text=" ".join(palabra))
    
def mostrar_pista():
    # Borrar el contenido anterior
    respuesta_texto.delete(1.0, tk.END)
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
ventana.configure(background="#2F4F4F")

tk.Wm.wm_title(ventana, "HANGMAN - DevGroup")

# Crear el label para mostrar el progreso del juego
progreso_label = tk.Label(ventana, text= palabra, font=("Arial", 16))
progreso_label.pack(side=tk.TOP, pady=10)


etiqueta = tk.Label(ventana, text = "HANGMAN DEV-GROUP", bg = "green", font=("Arial", 20, "bold"))
etiqueta.pack(side= tk.TOP, pady=10)
boton_enviar = tk.Button(ventana, text="Enviar", padx=10, pady=5, command=entrada) # Posicionamos el boton "Enviar"
boton_enviar.pack(side=tk.BOTTOM, pady=10)
entradaAlimentacion = tk.Text(ventana, width= 40, height=3) # Configuramos el tamaño de la ventana de alimentación
entradaAlimentacion.pack(side=tk.BOTTOM, pady=10) # Posicionamos la ventana de alimentación

# Configurar el botón para mostrar el historial
boton_mostrar_pista = tk.Button(ventana, text="Pedir pista", command=mostrar_pista)
boton_mostrar_pista.pack(side=tk.BOTTOM, pady=10)
# Configurar el botón para ocultar el historial
boton_ocultar_pista = tk.Button(ventana, text="Ocultar pista", command=ocultar_pista)

respuesta_texto = tk.Text(ventana, width=40, height=20)
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
# agregar historial de intentos
# agregar opcion de reiniciar
# agregar un menú, elegir usuario, mostrar el ranking, creditos, reiniciar y seleccionar dificultad.
# modificar la función "entrada" para que acepte la palabra completa
# hacer un login de usuario con una base de datos que contenga nombre de usuario y puntuación.
# hacer una clasificacion de los jugadores con mas puntaje.
