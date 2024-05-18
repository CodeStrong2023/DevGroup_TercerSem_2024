function reiniciar() {
  return location.reload();
}

function eleccionRand(max, min) {
  eleccionPC = Math.floor(Math.random() * (max - min + 1) + min);
  return eleccionPC;
}

function eleccion(jugada) {
  let resultado = "";
  if (jugada == 1) {
    resultado = "Piedra ✊";
  } else if (jugada == 2) {
    resultado = "Papel 🖐";
  } else if (jugada == 3) {
    resultado = "Tijera ✌";
  } else {
    resultado = "EROR. Mal elegido.";
  }
  return resultado;
}

// 1 será piedra, 2 será papel y 3 será tijera
let jugador = 0;
let triunfos = 0;
let derrotas = 0;
let pc = 0;

// jugador = prompt("Elige: 1 Piedra, 2 Papel, 3 Tijera")

while (triunfos < 3 && derrotas < 3) {
  pc = eleccionRand(3, 1);
  jugador = prompt("Elige: 1 Piedra, 2 Papel, 3 Tijera");
  // alert("Elige jugador" + jugador)

  alert("PC Elige: " + eleccion(pc) + "\n Tu eliges: " + eleccion(jugador));

  // Combate
  if (pc == jugador) {
    alert("Empate");
  } else if (jugador == 1 && pc == 3) {
    alert("Ganaste");
    triunfos = triunfos + 1;
  } else if (jugador == 2 && pc == 1) {
    alert("Ganaste");
    triunfos = triunfos + 1;
  } else if (jugador == 3 && pc == 2) {
    alert("Ganaste");
    triunfos = triunfos + 1;
  } else {
    alert("Perdiste");
    derrotas = derrotas + 1;
  }
}
alert("Ganaste " + triunfos + " veces. Perdiste " + derrotas + " veces.");
