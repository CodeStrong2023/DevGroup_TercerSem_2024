package Clase1.MundoPc.mundopc;

import ar.com.system2023.mundopc.*;

public class mundopc {
    public static void main(String[] args) {
        // objeto 1
        Monitor monitorHP = new Monitor("HP", 13);
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        // objeto 2
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);

        
        // objeto 3
        Monitor monitorSean = new Monitor("Sean", 32);
        Teclado tecladoSean = new Teclado("Bluetooth", "Sean");
        Raton ratonSean = new Raton("Bluetooth", "Sean");
        Computadora computadoraSean = new Computadora("Computadora Sean", monitorSean, tecladoSean, ratonSean);

        
        // objeto 4
        Monitor monitorNovik = new Monitor("Novik", 32);
        Teclado tecladoNovik = new Teclado("Bluetooth", "Novik");
        Raton ratonNovik = new Raton("Bluetooth", "Novik");
        Computadora computadoraNovik = new Computadora("Computadora Novik", monitorNovik, tecladoNovik, ratonNovik);

        
        // objeto 5
        Monitor monitorAxios = new Monitor("Axios", 32);
        Teclado tecladoAxios = new Teclado("Bluetooth", "Axios");
        Raton ratonAxios = new Raton("Bluetooth", "Axios");
        Computadora computadoraAxios = new Computadora("Computadora Axios", monitorAxios, tecladoAxios, ratonAxios);

        
        // objeto 6
        Monitor monitorVerbatim = new Monitor("Verbatim", 32);
        Teclado tecladoVerbatim = new Teclado("Bluetooth", "Verbatim");
        Raton ratonVerbatim = new Raton("Bluetooth", "Verbatim");
        Computadora computadoraVerbatim = new Computadora("Computadora Verbatim", monitorVerbatim, tecladoVerbatim, ratonVerbatim);

        
        // objeto 7
        Monitor monitorSamsung = new Monitor("Samsung", 32);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);

        
        // objeto 8
        Monitor monitorGenius = new Monitor("Genius", 32);
        Teclado tecladoGenius = new Teclado("Bluetooth", "Genius");
        Raton ratonGenius = new Raton("Bluetooth", "Genius");
        Computadora computadoraGenius = new Computadora("Computadora Genius", monitorGenius, tecladoGenius, ratonGenius);

        
        // objeto 9
        Monitor monitorLogi = new Monitor("Logi", 32);
        Teclado tecladoLogi = new Teclado("Bluetooth", "Logi");
        Raton ratonLogi = new Raton("Bluetooth", "Logi");
        Computadora computadoraLogi = new Computadora("Computadora Logi", monitorLogi, tecladoLogi, ratonLogi);

        
        // objeto 10
        Monitor monitorLG = new Monitor("LG", 32);
        Teclado tecladoLG = new Teclado("Bluetooth", "LG");
        Raton ratonLG = new Raton("Bluetooth", "LG");
        Computadora computadoraLG = new Computadora("Computadora LG", monitorLG, tecladoLG, ratonLG);

        // creamos orden
        Orden orden1 = new Orden(); // inicializamos el arreglo vacío
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(computadoraAxios);
        orden1.agregarComputadora(computadoraGenius);
        orden1.agregarComputadora(computadoraLG);
        orden1.agregarComputadora(computadoraLogi);
        orden1.agregarComputadora(computadoraNovik);
        orden1.agregarComputadora(computadoraSamsung);
        orden1.agregarComputadora(computadoraSean);
        orden1.agregarComputadora(computadoraVerbatim);
        orden1.mostrarOrden();
    }
}
