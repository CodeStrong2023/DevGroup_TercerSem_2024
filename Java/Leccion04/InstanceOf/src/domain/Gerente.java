package domain;


public class Gerente extends Empleado {
     private String departamento;
     
     public Gerente(String nombre, double sueldo, String depoartamento) {
          super(nombre, sueldo);
          this.departamento = departamento;     
     }
     @Override
     //Sobreescribimos el metodo
      public String obtenerDetalles() {
          return super.obtenerDetalles()+", Depatamento: "+this.departamento;
      }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }
      
      
}
