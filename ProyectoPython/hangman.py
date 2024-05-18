# import pymongo
# import respuesta
# import mongodb
import googleapi as chatbot
import tkinter as tk
import google.generativeai as genai

historial = []
# ALIMENTACION
def entrada():
    pregunta =  entradaAlimentacion.get("1.0","end-1c")
    historial.append({"Role" : "User", "content" : pregunta})
    response = chatbot.model.generate_content(pregunta)
    historial.append({"Role" : "Hangman", "content" : response.text})
    entradaAlimentacion.delete(1.0, tk.END) # BORRA LOS TEXTOS INGRESADOS


def mostrar_historial():
    # Borrar el contenido anterior
    respuesta_texto.delete(1.0, tk.END)
    # Mostrar el historial en la ventana de respuesta
    for mensaje in historial:
        respuesta_texto.insert(tk.END, f"{mensaje['Role']}: {mensaje['content']}\n")
    # Deshabilitar el widget para hacerlo de solo lectura
    respuesta_texto.config(state=tk.DISABLED)
    boton_mostrar_historial.pack_forget()
    boton_ocultar_historial.pack(side=tk.BOTTOM, pady=10)
    # Mostrar la ventana de respuesta
    respuesta_texto.pack(side=tk.BOTTOM, pady=10)
    
def ocultar_historial():
    # Ocultar la ventana de respuesta
    respuesta_texto.pack_forget()
    # Ocultar el botón "Ocultar Historial" y mostrar el botón "Mostrar Historial"
    boton_ocultar_historial.pack_forget()
    boton_mostrar_historial.pack(side=tk.BOTTOM, pady=10)
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(background="#2F4F4F")
tk.Wm.wm_title(ventana, "HANGMAN - DevGroup")
etiqueta = tk.Label(ventana, text = "HANGMAN DEV-GROUP", bg = "green", font=("Arial", 20, "bold"))
etiqueta.pack(side= tk.TOP, pady=10)
boton_enviar = tk.Button(ventana, text="Enviar", padx=10, pady=5, command=entrada) # Posicionamos el boton "Enviar"
boton_enviar.pack(side=tk.BOTTOM, pady=10)
entradaAlimentacion = tk.Text(ventana, width= 40, height=3) # Configuramos el tamaño de la ventana de alimentación
entradaAlimentacion.pack(side=tk.BOTTOM, pady=10) # Posicionamos la ventana de alimentación

# Configurar el botón para mostrar el historial
boton_mostrar_historial = tk.Button(ventana, text="Mostrar Historial", command=mostrar_historial)
boton_mostrar_historial.pack(side=tk.BOTTOM, pady=10)
# Configurar el botón para ocultar el historial
boton_ocultar_historial = tk.Button(ventana, text="Ocultar Historial", command=ocultar_historial)

respuesta_texto = tk.Text(ventana, width=40, height=20)
ventana.mainloop()


# PARA HACER
# Crear ciclo while con la logica del juego
# este deberá contener una variable "intentos" que al alcanzar el valor 5 
# el ciclo while se detiene y el usuario pierde
#       O la cabeza está siempre
#      /|\
#      /\
#