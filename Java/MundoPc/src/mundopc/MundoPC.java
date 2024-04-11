
package mundopc;

import ar.com.system2024.mundo.pc.*;


public class MundoPC {
    public static void main(String[] args) {
        //Objeto1
        Monitor monitorHP = new Monitor("HP", 13);
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //Creamos otros objetos de diferente marca
        
        //Objeto2
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
        //Objeto3
        Monitor monitorSamsung = new Monitor("Samsung", 22);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);
        
        //Objeto4
        Monitor monitorAsus = new Monitor("Asus", 15);
        Teclado tecladoAsus = new Teclado("Bluetooth", "Asus");
        Raton ratonAsus = new Raton("Bluetooth", "Asus");
        Computadora computadoraAsus = new Computadora("Computadora Asus", monitorAsus, tecladoAsus, ratonAsus);
        
        //Objeto5
        Monitor monitorApple = new Monitor("Apple", 28);
        Teclado tecladoApple = new Teclado("Bluetooth", "Apple");
        Raton ratonApple = new Raton("Bluetooth", "Apple");
        Computadora computadoraApple = new Computadora("Computadora Apple", monitorApple, tecladoApple, ratonApple);
        
        //Objeto6
        Monitor monitorLenovo = new Monitor("Lenovo", 13);
        Teclado tecladoLenovo = new Teclado("Bluetooth", "Lenovo");
        Raton ratonLenovo = new Raton("Bluetooth", " Lenovo");
        Computadora computadoraLenovo = new Computadora("Computadora Lenovo", monitorLenovo, tecladoLenovo, ratonLenovo);
        
        //Objeto7
        Monitor monitorMSI = new Monitor("MSI", 29);
        Teclado tecladoMSI = new Teclado("Bluetooth", "MSI");
        Raton ratonMSI = new Raton("Bluetooth", "MSI");
        Computadora computadoraMSI = new Computadora("Computadora MSI", monitorMSI, tecladoMSI, ratonMSI);
        
        //Objeto8
        Monitor monitorHuawei = new Monitor("Huawei", 14);
        Teclado tecladoHuawei = new Teclado("Bluetooth", "Huawei");
        Raton ratonHuawei = new Raton("Bluetooth", "Huawei");
        Computadora computadoraHuawei = new Computadora("Computadora Huawei", monitorHuawei, tecladoHuawei, ratonHuawei);
        
        //Objeto9
        Monitor monitorAcer = new Monitor("Acer ", 20);
        Teclado tecladoAcer = new Teclado("Bluetooth", "Acer ");
        Raton ratonAcer = new Raton("Bluetooth", "Acer ");
        Computadora computadoraAcer = new Computadora("Computadora Acer", monitorAcer, tecladoAcer, ratonAcer);
        
        //Objeto10
        Monitor monitorRedragon = new Monitor("Redragon", 32);
        Teclado tecladoRedragon = new Teclado("Bluetooth", "Redragon");
        Raton ratonRedragon = new Raton("Bluetooth", "Redragon");
        Computadora computadoraRedragon = new Computadora("Computadora Redragon", monitorRedragon, tecladoRedragon, ratonRedragon);
        Orden orden1 = new Orden(); //Inicializamos el arreglo vacio
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(computadoraSamsung);
        orden1.agregarComputadora(computadoraAsus);
        orden1.agregarComputadora(computadoraApple);
        orden1.agregarComputadora(computadoraLenovo);
        orden1.agregarComputadora(computadoraMSI);
        orden1.agregarComputadora(computadoraHuawei);
        orden1.agregarComputadora(computadoraAcer );
        orden1.agregarComputadora(computadoraRedragon);
        orden1.mostrarOrden();
        Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2
        Computadora computadoraVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonGamer);
        orden2.agregarComputadora(computadoraVarias);
        orden2.mostrarOrden();
        
        //Crear mas objetos de tipo computadora con todos sus elementos
        //Completar una lista en el objeto orden1 que llegue a los 10 elementos
        //Probar de esta manera los métodos al maximo rendimiento
        
    }
    
}
