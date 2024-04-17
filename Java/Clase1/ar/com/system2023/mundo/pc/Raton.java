
package ar.com.system2023.mundo.pc;

public class Raton extends DispositivoEntrada{
    private static int contadorRatones ;
    private final int idRaton;
    
    public Raton(String tipoEntrada, String Marca){
        super(tipoEntrada, Marca);
        this.idRaton = ++Raton.contadorRatones;

    }

    @Override
    public String toString() {
        return "Raton{" + "idRaton=" + idRaton +", " +super.toString()+'}';
    }
}
