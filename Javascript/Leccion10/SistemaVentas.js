class Producto{
    static contadorProductos = 0;
    constructor(nombre, precio){
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto(){
        return this._idProducto;
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get precio(){
        return this._precio;
    }
    set precio(precio){
        this._precio = precio;
    }

    toString(){
    return 'idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}';
    }
} // fin de la clase producto

class Orden{
    static contadorOrdenes= 0;
    static getMAX_PRODUCTOS(){//Simula una constante
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    }

    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto); //Tenemos 2 tipos de sintaxis
            //this._productos[this._contadorProductosAgregados++] = producto; //segunda sintaxis
        }
        else{
            console.log("No se pueden agregar mas productos");
        }
    }//Fin del método gregarProducto

    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        }//Fin ciclo for
        return totalVenta;
    }//Fin del metodo calcular total
    mostrarOrden(){
        let productosOrden = " ";
        for(let producto of this._productos){
            productosOrden += '\n{ '+producto.toString()+" }";
        }//Fin del ciclo For
        console.log('Orden: ${this._idOrden}, Total: $${this._calcularTotal()}, Productos: ${productosOrden}');
    }//Fin metodo mostrarOrden
}//Fin de la clase Orden

let producto1 = new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
let producto3 = new Producto('Cinturón', 50)
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden1.mostrarOrden();
orden2.mostrarOrden();