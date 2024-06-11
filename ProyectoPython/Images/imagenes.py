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

    return img
