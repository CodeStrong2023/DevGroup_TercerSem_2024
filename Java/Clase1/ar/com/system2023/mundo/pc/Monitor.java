
package ar.com.system2023.mundo.pc;


public class Monitor {
    private static int contadorMonitores;
    private final int idMonitor;
    private String marca;
    private double tamanio;
    
    //Constructor 1
    private Monitor(){
        this.idMonitor = ++Monitor.contadorMonitores;
        
        
    
  }
    //Constructor 2
    public Monitor( String marca, double tamanio){
        this(); //Llamado al constructor vacio 
        this.marca = marca;
        this.tamanio = tamanio;
        
        
        
    }

    public static int getContadorMonitores() {
        return contadorMonitores;
    }

    public static void setContadorMonitores(int contadorMonitores) {
        Monitor.contadorMonitores = contadorMonitores;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getTamanio() {
        return this.tamanio;
    }

    public void setTamanio(double tamanio) {
        this.tamanio = tamanio;
    }
    
    //Ingresamos manualmente el getidMonitor
    public int getidMonitor(){
        return this.idMonitor;
    }

    @Override
    public String toString() {
        return "Monitor{" + "idMonitor=" + idMonitor + ", marca=" + marca + ", tamanio=" + tamanio + '}';
    }
    
}
