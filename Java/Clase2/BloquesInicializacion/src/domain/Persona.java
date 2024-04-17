
package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ //Bloque de inicialización estático
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersonas;
        //idPersona = 10; Salta error por que no es un atributo estático
        
        
        
    }
    
    { //Bloque de inicialización no estático(contexto dinámico)
        System.out.println("Ejecución del bloque no estático");
        this.idPersona = Persona.contadorPersonas++; //Incrementamos el atributo
    }
    
    public Persona(){ 
        System.out.println("Ejecución del constructor");
        
    }

    public int getIdPersona() {
        return idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }


}
