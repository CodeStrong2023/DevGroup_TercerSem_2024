
package paquete2;

public class Clase4 {
    private String atributoPrivado = "Atributo Privado";
    
    private Clase4(){
        System.out.println("Constructor privado");
    }
    
    //Creamos un constructor public para poder crear Objetos
    public Clase4(String argumento){ //Aca se puede llamar al constructor vacio
        this();
        System.out.println("Constructor publico");
    }
    
    //Método private
    private void metodoPrivado(){
        System.out.println("Método privado");
    }

    public String getAtributoPrivado() {
        return atributoPrivado;
    }

    public void setAtributoPrivado(String atributoPrivado) {
        this.atributoPrivado = atributoPrivado;
    }
    
    
}


