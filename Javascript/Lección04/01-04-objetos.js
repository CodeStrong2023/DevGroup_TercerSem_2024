let x = 10; 
console.log(x.length); 
console.log('Tipos primitivos'); 
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28, 
    idioma: "ES",
    get lang(){
        return this.idioma.toUpperCase(); // Convierte mayúsculas a minúsculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ // metodo o funcion en JavaScript
        return this.nombre + ' ' + this.apellido;
    }, 
    get nombreEdad(){ // Este es el metodo get
        return "El nombre es: " + this.nombre + " edad: " + this.edad
    },
    
}
console.log(persona.nombre); // "Carlos"
console.log(persona.apellido); // "Gil"
console.log(persona.email); // "cgil@gmail.com"
console.log(persona.edad); // 30
console.log(persona); // { nombre: 'Carlos', apellido: 'Gil', email: 'cgil@gmail.com', edad: 30}
console.log(persona.nombreCompleto()); // "Carlos Gil"
console.log('Ejecutando con un objeto'); 
let persona2 = new Object(); //debe crear un nuevo objeto en memoria 
persona2.nombre = 'Juan';
persona2.direccion = 'salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono); 5492618282821
console.log('Creamos un nuevo objeto'); 
console.log(persona["apellido"]) //accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in'); 
console.log('Usamos ciclo for in')
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log('Cambiamos y eliminamos un error'); 
persona.apellida = "Betancud"; //cambiamos dinamicamente un valor de un objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto:
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Numero 2: a traves del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: la funcion Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: utilizaremos el metodo JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el método get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el método get y set para idiomas");
persona.lang = "es";
console.log(persona.lang);

function Persona3(nombre, apellido, email){ // Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com");
padre.nombre = "Luis";
console.log(padre);

let madre = new Persona3("Laura", "Contrera", "contreral@gmail.com");
console.log(madre);