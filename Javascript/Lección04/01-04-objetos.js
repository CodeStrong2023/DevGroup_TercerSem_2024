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