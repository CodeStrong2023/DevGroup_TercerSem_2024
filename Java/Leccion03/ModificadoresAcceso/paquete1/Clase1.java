package ModificadoresAcceso.paquete1;

public class Clase1{
    public String atributoPublic = "Valor atributo public";

    public Clase1(){
        System.out.println("Constructor public");
    }

    public void metodoPublico(){
        System.out.println("Método public");
    }
    protected void metodoProtected(){
        System.out.println("Método protected");
    }
}