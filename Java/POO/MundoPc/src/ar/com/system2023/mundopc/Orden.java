package ar.com.system2023.mundopc;

public class Orden {
    private final int idOrden;
    private Computadora computadoras[]; //Arreglo objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;
    private int contadorComputadora;

    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadoras = new Computadora[Orden.MAX_COMPUTADORAS];
    }
    public void agregarComputadora(Computadora computadora){
        if(this.contadorComputadora < Orden.MAX_COMPUTADORAS){
            this.computadoras[this.contadorComputadora++] = computadora;
        }
        else{
            System.out.println("Has superado el limite: " + Orden.MAX_COMPUTADORAS);
        }
    }

    //Mostrar orden
    public void mostrarOrden(){
        System.out.println("Orden #: "+ this.idOrden);
        System.out.println("Computadoras de la orden #: " + this.idOrden);
        for(int i = 0; i < contadorComputadora; i++){
            System.out.println(this.computadoras[i]);
        }
    }
}
