package mundopc;
import ar.com.system2023.mundopc.*;
public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP",13);
        Teclado tecladoHP = new Teclado("Bluetooth","HP");
        Raton ratonHP = new Raton("Bluetooth","HP");
        Computadora computadoraHP = new Computadora("Computadora HP",monitorHP,tecladoHP,ratonHP);

        //Creamos objetos de diferentes marcas

        Monitor monitorLenovo = new Monitor("Lenovo",32);
        Teclado tecladoLogiTech = new Teclado("Bluetooth","LogiTech");
        Raton ratonLOGI = new Raton("Bluetooth","LogiTech");
        Computadora computadoraGamer = new Computadora("Lenovo Legion",monitorLenovo,tecladoLogiTech,ratonLOGI);

        Orden orden1 = new Orden(); //Inicializamos el arreglo
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.mostrarOrden();

    }
}
