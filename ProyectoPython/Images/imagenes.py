from PIL import Image, ImageTk

def cargar_imagenes(root):
    img = {}
    portada = Image.open("Images/HANGMAN.jpeg")
    portada = portada.resize((800, 800), Image.LANCZOS)
    img["portadaIMG"] = ImageTk.PhotoImage(portada, master=root)

    HANGMAN = Image.open("Images/HANGMANlabel.jpeg")
    HANGMAN = HANGMAN.resize((250, 100), Image.LANCZOS)
    img["HANGMANimg"] = ImageTk.PhotoImage(HANGMAN, master=root)

    ahorcado1 = Image.open("Images/ahorcado1.jpg")
    img["ahorcado1img"] = ImageTk.PhotoImage(ahorcado1, master=root)

    ahorcado2 = Image.open("Images/ahorcado2.jpg")
    img["ahorcado2img"] = ImageTk.PhotoImage(ahorcado2, master=root)

    ahorcado3 = Image.open("Images/ahorcado3.jpg")
    img["ahorcado3img"] = ImageTk.PhotoImage(ahorcado3, master=root)

    ahorcado4 = Image.open("Images/ahorcado4.jpg")
    img["ahorcado4img"] = ImageTk.PhotoImage(ahorcado4, master=root)

    ahorcado5 = Image.open("Images/ahorcado5.jpg")
    img["ahorcado5img"] = ImageTk.PhotoImage(ahorcado5, master=root)

    ahorcado6 = Image.open("Images/ahorcado6.jpg")
    img["ahorcado6img"] = ImageTk.PhotoImage(ahorcado6, master=root)

    boton_registroIMG = Image.open("Images/BotonRegistro.png")
    img["boton_registroIMG"] = ImageTk.PhotoImage(boton_registroIMG, master=root)

    boton_loginIMG = Image.open("Images/BotonIniciarSesion.png")
    img["boton_loginIMG"] = ImageTk.PhotoImage(boton_loginIMG, master=root)

    boton_salirIMG = Image.open("Images/BotonSalir.png")
    img["boton_salirIMG"] = ImageTk.PhotoImage(boton_salirIMG, master=root)

    boton_clasificacionIMG = Image.open("Images/BotonClasificacion.png")
    img["boton_clasificacionIMG"] = ImageTk.PhotoImage(boton_clasificacionIMG, master=root)

    boton_iniciarsesionIMG = Image.open("Images/BotonIniciarSesionMini.png")
    img["boton_iniciarsesionIMG"] = ImageTk.PhotoImage(boton_iniciarsesionIMG, master=root)

    boton_registrarIMG = Image.open("Images/BotonRegistroMini.png")
    img["boton_registrarIMG"] = ImageTk.PhotoImage(boton_registrarIMG, master=root)

    boton_volverIMG = Image.open("Images/BotonVolver.png")
    img["boton_volverIMG"] = ImageTk.PhotoImage(boton_volverIMG, master=root)

    boton_reglasIMG = Image.open("Images/BotonReglas.png")
    img["boton_reglasIMG"] = ImageTk.PhotoImage(boton_reglasIMG, master=root)

    boton_aceptar = Image.open("Images/BotonAceptar.png")
    img["boton_aceptarIMG"] = ImageTk.PhotoImage(boton_aceptar, master=root)

    usuarioIMG = Image.open("Images/usuario.png")
    img["usuarioIMG"] = ImageTk.PhotoImage(usuarioIMG, master=root)

    puntaje_usuario = Image.open("Images/UserRankingLabel.png")
    img["puntaje_usuarioIMG"] = ImageTk.PhotoImage(puntaje_usuario, master=root)

    palabras_acertadas_img = Image.open("Images/PalabrasAcertadasLabel.png")
    img["palabras_acertadasIMG"] = ImageTk.PhotoImage(palabras_acertadas_img, master=root)

    contrasena = Image.open("Images/contraseña.png")
    img["contrasenaIMG"] = ImageTk.PhotoImage(contrasena, master=root)

    contrasenaVacia = Image.open("Images/contraseñaVacia.png")
    img["contrasenaVaciaIMG"] = ImageTk.PhotoImage(contrasenaVacia, master=root)

    contrasenaActualizada = Image.open("Images/contraseñaActualizada.png")
    img["contrasenaActualizadaIMG"] = ImageTk.PhotoImage(contrasenaActualizada, master=root)
    
    usuarioVacio = Image.open("Images/usuarioVacio.png")
    img["usuarioVacioIMG"] = ImageTk.PhotoImage(usuarioVacio, master=root)
    
    usuarioExistente = Image.open("Images/usuarioExistente.png")
    img["usuarioExistenteIMG"] = ImageTk.PhotoImage(usuarioExistente)

    nro1 = Image.open("Images/nro1.png")
    img["nro1"] = ImageTk.PhotoImage(nro1, master=root)

    nro2 = Image.open("Images/nro2.png")
    img["nro2"] = ImageTk.PhotoImage(nro2, master=root)

    nro3 = Image.open("Images/nro3.png")
    img["nro3"] = ImageTk.PhotoImage(nro3, master=root)

    nro4 = Image.open("Images/nro4.png")
    img["nro4"] = ImageTk.PhotoImage(nro4, master=root)

    nro5 = Image.open("Images/nro5.png")
    img["nro5"] = ImageTk.PhotoImage(nro5, master=root)

    nro6 = Image.open("Images/nro6.png")
    img["nro6"] = ImageTk.PhotoImage(nro6, master=root)

    nro7 = Image.open("Images/nro7.png")
    img["nro7"] = ImageTk.PhotoImage(nro7, master=root)

    nro8 = Image.open("Images/nro8.png")
    img["nro8"] = ImageTk.PhotoImage(nro8, master=root)

    nro9 = Image.open("Images/nro9.png")
    img["nro9"] = ImageTk.PhotoImage(nro9, master=root)

    nro10 = Image.open("Images/nro10.png")
    img["nro10"] = ImageTk.PhotoImage(nro10, master=root)

    nombre = Image.open("Images/nombre.png")
    img["nombre"] = ImageTk.PhotoImage(nombre, master=root)

    puntaje = Image.open("Images/puntaje.png")
    img["puntaje"] = ImageTk.PhotoImage(puntaje, master=root)

    palabras_adivinadas = Image.open("Images/palabras_adivinadas.png")
    img["palabras_adivinadas"] = ImageTk.PhotoImage(palabras_adivinadas, master=root)

    return img
