
class Persona{ //Clase padre

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre =nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
    
}

let persona1 = new Persona('Martin', 'Perez')
console.log(persona1._nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
persona1.apellido = 'Lopez'
console.log(persona1._apellido);

//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara')
console.log(persona2._nombre);
persona2.nombre = 'Maria Laura'
console.log(persona2._nombre);
persona2.apellido = 'Benitez'
console.log(persona2._apellido);
//console.log(persona2)
