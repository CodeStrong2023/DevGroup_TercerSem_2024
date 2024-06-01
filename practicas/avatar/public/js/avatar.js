document
  .getElementById("boton-personaje")
  .addEventListener("click", function () {
    const radios = document.getElementsByName("personaje");
    let personajeElegido;
    for (const radio of radios) {
      if (radio.checked) {
        personajeElegido = radio.value;
        break;
      }
    }
    if (personajeElegido) {
      alert("Personaje seleccionado: " + personajeElegido);
    } else {
      alert("No se ha seleccionado ningún personaje.");
    }
  });

document.addEventListener("DOMContentLoaded", function () {
  const personajes = ["Zuko", "Katara", "Aang", "Toph"];

  function seleccionarPersonajeComputadora() {
    const indiceAleatorio = Math.floor(Math.random() * personajes.length);
    const personajeComputadora = personajes[indiceAleatorio];

    return personajeComputadora;
  }

  let personajeComputadora = seleccionarPersonajeComputadora();

  const personajeElemento = document.getElementById("personaje-computadora");
  personajeElemento.textContent =
    "Personaje seleccionado por la computadora: " + personajeComputadora;
});
