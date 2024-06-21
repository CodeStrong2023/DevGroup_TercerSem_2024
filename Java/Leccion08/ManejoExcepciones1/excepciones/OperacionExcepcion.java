package Java.Leccion08.ManejoExcepciones1.excepciones;

public class OperacionExcepcion extends RunTimeException{
    //Constructor
    public OperacionExcepcion(String mensaje){
        super(mensaje);
    }
}