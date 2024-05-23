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
