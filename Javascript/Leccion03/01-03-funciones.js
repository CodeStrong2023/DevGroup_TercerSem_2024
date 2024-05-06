miFuncion(8,2); //Esto se le conoce como hosting (se puede llamar a la funcion antes de que sea definida)

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a+b));
    return a+b;
}

//Llamamos a la funcion
miFuncion(5,4);

let resultado = miFuncion(6,7);
console.log(resultado);

//Declaramos una funcion de tipo "expresion o anonima"
let x = function(a, b){return a+b}; //necesita cierre con punto y coma
resultado = x(5,6); //al llamar se pone la variable y parentesis
console.log(resultado);

//Funciones de tipo self e invoking
(function(a, b){
    console.log('Ejecutando la funcion: '+(a+b));
})(9,6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}

miFuncionDos(5, 7, 3, 6);

//toSting
var miFuncionTexto = miFuncionDos.toString(); //convierte la funcion a texto
console.log(miFuncionTexto);

