
package ar.com.system2024.mundo.pc;


public class Orden {
    private final int idOrden;
    private Computadora computadora[]; // Arreglo de objetos 
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;
    private int contadorComputadora;
    
    public Orden(){ //Contructor1
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];
    }
    
    //Constructor2 método para agregar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora){
        if(this.contadorComputadora < Orden.MAX_COMPUTADORAS){
            this.computadora[this.contadorComputadora++] = computadora;
        }
        else{
            System.out.println("Has superado el limite: " + Orden.MAX_COMPUTADORAS);
        }
    }
    
    //Contructor3 método para mostrar orden
    public void mostrarOrden(){
        System.out.println("Orden #:" + this.idOrden);
        System.out.println("Computadoras de la orden: " + this.idOrden);
        for (int i = 0;  i < this.contadorComputadora; i++) {
            System.out.println(this.computadora[i]);
            
        }
    }
}
