package ModificadoresAcceso.test;

import ModificadoresAcceso.paquete1.Clase1;

public class TestModificadoresAcceso {
    public static void main(String[] args) {
      Clase1 clase1 = new Clase1();
      System.out.println("Clase1 = "+ clase1.atributoPublic);
      clase1.metodoPublico();
    }
}
