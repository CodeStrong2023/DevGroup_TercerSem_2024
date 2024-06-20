package Java.Leccion08.ManejoExcepciones1.aritmetica;

import Java.Leccion08.ManejoExcepciones1.excepciones.OperacionExcepcion;

public class Aritmetica {
    public static int division(int numerador, int denominador){
        if (denominador==0){
            throw new OperacionExcepcion("División entre cero");
        }
        return numerador/denominador;
    }
}
