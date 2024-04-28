
package paquete1;

class Clase2 extends Clase1{
    String atributoDefault = "Valor del atributo Default";
    
    //Clase2(){
    //  System.out.println("Constructor Default");
    //}
    
    Clase2(){
        super();
        this.atributoDefault = "Modificación del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
    
    void metodoDefault(){
        System.out.println("Método Default");
    }
}
