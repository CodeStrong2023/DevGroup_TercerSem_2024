let ataqueJugador;
let ataqueEnemigo;

function iniciarJuego() {
  let botonPersonajeJugador = document.getElementById("boton-personaje");
  botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador);

  let botonPunio = document.getElementById("boton-punio"); //Ahora creamos un escuchador de eventos
  botonPunio.addEventListener("click", ataquePunio);
  let botonPatada = document.getElementById("boton-patada");
  botonPatada.addEventListener("click", ataquePatada);
  let botonBarrida = document.getElementById("boton-barrida");
  botonBarrida.addEventListener("click", ataqueBarrida);
}

function seleccionarPersonajeJugador() {
  let inputZuko = document.getElementById("zuko");
  let inputKatara = document.getElementById("katara");
  let inputAang = document.getElementById("aang");
  let inputToph = document.getElementById("toph");
  let spanPersonajeJugador = document.getElementById("personaje-jugador");

  if (inputZuko.checked) {
    spanPersonajeJugador.innerHTML = "Zuko";
  } else if (inputKatara.checked) {
    spanPersonajeJugador.innerHTML = "Katara";
  } else if (inputAang.checked) {
    spanPersonajeJugador.innerHTML = "Aang";
  } else if (inputToph.checked) {
    spanPersonajeJugador.innerHTML = "Toph";
  } else {
    alert("Selecciona un personaje");
  }
  seleccinarPersonajeEnemigo();
}

function seleccinarPersonajeEnemigo() {
  //esta función va dentro de seleccionarPersonajeJugador() al final
  let personajeAleatorio = aleatorio(1, 4); //A continuación creamos las variables para cada personaje
  let spanPersonajeEnemigo = document.getElementById("personaje-enemigo");

  //comenzamos con la lógica
  if (personajeAleatorio == 1) {
    spanPersonajeEnemigo.innerHTML = "Zuko";
  } else if (personajeAleatorio == 2) {
    spanPersonajeEnemigo.innerHTML = "Katara";
  } else if (personajeAleatorio == 3) {
    spanPersonajeEnemigo.innerHTML = "Aang";
  } else {
    spanPersonajeEnemigo.innerHTML = "Toph";
  }
}

function ataquePunio() {
  //Modificamos la variable global ataqueJugador
  ataqueJugador = "Punio";
  ataqueAleatorioEnemigo();
}

function ataquePatada() {
  //Modificamos la variable global ataqueJugador
  ataqueJugador = "Patada";
  ataqueAleatorioEnemigo();
}

function ataqueBarrida() {
  //Modificamos la variable global ataqueJugador
  ataqueJugador = "Barrida";
  ataqueAleatorioEnemigo();
}

function ataqueAleatorioEnemigo() {
  //Ahora ocupando la variable global nueva le decimos el ataque y necesitamos la función aleatorio
  let ataqueAleatorio = aleatorio(1, 3);

  if (ataqueAleatorio == 1) {
    ataqueEnemigo = "Punio";
  } else if (ataqueAleatorio == 2) {
    ataqueEnemigo = "Patada";
  } else {
    ataqueEnemigo = "Barrida";
  }

  combate();
}

function combate() {
  if (ataqueEnemigo == ataqueJugador) {
    crearMensaje("EMPATE");
  } else if (ataqueJugador == "Punio" && ataqueEnemigo == "Barrida") {
    crearMensaje("GANASTE");
  } else if (ataqueJugador == "Patada" && ataqueEnemigo == "Punio") {
    crearMensaje("GANASTE");
  } else if (ataqueJugador == "Barrida" && ataqueEnemigo == "Patada") {
    crearMensaje("GANASTE");
  } else {
    crearMensaje("PERDISTE");
  }
}

function crearMensaje(resultado) {
  let sectionMensaje = document.getElementById("mensajes");
  let parrafo = document.createElement("p");

  parrafo.innerHTML =
    "Tu personaje atacó con " +
    ataqueJugador +
    ", el personaje del enemigo atacó con " +
    ataqueEnemigo +
    " - " +
    resultado;

  sectionMensaje.appendChild(parrafo);
}

function aleatorio(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

window.addEventListener("load", iniciarJuego);
