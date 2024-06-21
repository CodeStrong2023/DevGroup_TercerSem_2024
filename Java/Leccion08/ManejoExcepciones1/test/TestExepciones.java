package Java.Leccion08.ManejoExcepciones1.test;

import static Java.Leccion08.ManejoExcepciones1.aritmetica.Aritmetica.division;

import Java.Leccion08.ManejoExcepciones1.excepciones.OperacionExcepcion;

public class TestExepciones {
    public static void main(String[] args) {
        int resultado = 0;
       try{
            resultado = division(10, 0);
       }catch(OperacionExcepcion e){
        System.out.println("Ocurrió un error de tipo OperacionExcepcion");
        System.out.println(e.getMessage());
       }catch(Exception e){
        System.out.println("Ocurrió un error");
        e.printStackTrace(System.out); // se conoce como la pila de excepciones
        System.out.println(e.getMessage());
        }
       finally{
        System.out.println("Se revisó la división entre cero");
       }
        System.out.println("La variable de resultado tiene como valor: " +resultado);
    }
}
