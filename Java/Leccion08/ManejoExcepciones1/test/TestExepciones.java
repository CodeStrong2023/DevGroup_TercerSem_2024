package Java.Leccion08.ManejoExcepciones1.test;

public class TestExepciones {
    public static void main(String[] args) {
        int resultado = 0;
   //     try{
            resultado = 10/0;
   //     } catch(Exception e){
   //         System.out.println("Ocurrió un error");
   //         e.printStackTrace(System.out); // se conoce como la pila de excepciones
   //     }
        System.out.println("La variable de resultado tiene como valor: " +resultado);
    }
}
