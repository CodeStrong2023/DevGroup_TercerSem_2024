let x = 10; 
console.log(x.length); 

//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30, 
    nombreCompleto: function(){ // metodo o funcion en JavaScript
        return this.nombre + ' ' + this.apellido;
    }  
}

console.log(persona.nombre); // "Carlos"
console.log(persona.apellido); // "Gil"
console.log(persona.email); // "cgil@gmail.com"
console.log(persona.edad); // 30
console.log(persona); // { nombre: 'Carlos', apellido: 'Gil', email: 'cgil@gmail.com', edad: 30}
console.log(persona.nombreCompleto()); // "Carlos Gil"

let persona2 = new Object(); //debe crear un nuevo objeto en memoria 
persona2.nombre = 'Juan';
persona2.direccion = 'salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono); 5492618282821
console.log('Creamos un nuevo objeto');
console.log(persona["apellido"]) //accedemos como si fuera un arreglo

console.log('Usamos ciclo for in')
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('cambiamos y eliminamos el error')
persona.apellida = "Betancud"; //cambiamos dinamicamente un valor de un objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log("Distitas formas de imprimir un objeto: FORMA 1")
console.log(persona.nombre+', '+persona.apellido)
console.log("Distitas formas de imprimir un objeto: FORMA 2")
//Numero 2: A través del ciclo for in
for(nombreCompleto in persona){
    console.log(persona[nombreCompleto]); 
}
console.log("Distitas formas de imprimir un objeto: FORMA 3")
//Numero 3: La función Object.values()
let personaArray = Object.values(persona);
console.log(personaArray);

//Número 4: Utilizaremos el metodo json.stringify
console.log("distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);
