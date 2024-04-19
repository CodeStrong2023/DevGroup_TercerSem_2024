// Ciclos while

let contador = 0;

while (contador < 3) {
  console.log(contador);
  contador++;
}
console.log("Fin del ciclo while");

// Ciclos Do While

let conteo = 0;
do {
  console.log(conteo);
  conteo++;
} while (conteo < 3);
console.log("Fin del ciclo do while");

// Ciclos for

for (let contando = 0; contando < 3; contando++) {
  console.log(contando);
}
console.log("Fin del ciclo for");

// Palabra reservada break

for (let contando = 0; contando <= 10; contando++) {
  if (contando % 2 == 0) {
    console.log(contando); // Muestra los npumeros pares
    break;
  }
}
console.log("Termina el ciclo al mostrar el primer n° par");

// Palabra reservada continue y etiquetas labels

inicio: for (let contando = 0; contando <= 10; contando++) {
  if (contando % 2 !== 0) {
    continue inicio; // Ir a la siguiente iteración
  }
  console.log(contando);
}
console.log("Termina el ciclo");
