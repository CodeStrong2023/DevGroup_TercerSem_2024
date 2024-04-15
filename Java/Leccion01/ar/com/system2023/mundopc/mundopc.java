package ar.com.system2023.mundopc;

public class mundopc {
    public static void main(String[] args) {
        // definimos var, creamos objetos

        Monitor monitorHP = new Monitor("HP ", 13); // importamos la clase
        Teclado tecladoHP = new Teclado("Bluetooth ", " HP");
        Raton ratonHP = new Raton("Bluetooth ", "HP");
        Computadora computadoraHP = new Computadora("ComputadoraHP ", monitorHP, tecladoHP, ratonHP);

        Monitor monitorGamer = new Monitor("Gamer ", 32); 
        Teclado tecladoGamer = new Teclado("Bluetooth ", "Gamer ");
        Raton ratonGamer = new Raton("Bluetooth ", "Gamer");
        Computadora computadoraGamer = new Computadora("ComputadoraGamer ", monitorGamer, tecladoGamer, ratonGamer);

        Monitor monitorLogitech = new Monitor("Logitech ", 38); 
        Teclado tecladoLogitech = new Teclado("Bluetooth ", " Logitech ");
        Raton ratonLogitech = new Raton("Bluetooth ", " Logitech ");
        Computadora computadoraLogitech = new Computadora("ComputadoraLogitech ", monitorLogitech, tecladoLogitech, ratonLogitech);
        
        Computadora computadoraVar4 = new Computadora("Computadoras de distintas marcas", monitorLogitech, tecladoHP, ratonGamer);
        Computadora computadoraVar5 = new Computadora("Computadoras de distintas marcas", monitorHP, tecladoGamer, ratonLogitech);
        
        // obj de tipo orden
        Orden orden1 = new Orden(); // arreglo vacio
        Orden orden2 = new Orden();
        Orden orden3 = new Orden();
        Orden orden4 = new Orden();
        Orden orden5 = new Orden();


        orden1.agregarComputadora(computadoraGamer);
        orden2.agregarComputadora(computadoraHP);
        orden3.agregarComputadora(computadoraLogitech);
        orden4.agregarComputadora(computadoraVar4);
        orden5.agregarComputadora(computadoraVar5);


        orden5.mostrarOrden();
        orden4.mostrarOrden();
        orden3.mostrarOrden();
        orden2.mostrarOrden();
        orden1.mostrarOrden(); 
    }
}
