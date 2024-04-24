
package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ //bloque de inicializacion estatico
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersonas;
        // idPersona = 10;     No es un atributo estatico por eso tenemos un error
    }
    
    { //bloque de inicializacion NO estatico (contexto dinamico)
        System.out.println("Ejecucioin del bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++;  //incrementamos el atributo
    }
    
    // los bloques de inicializacion se ejecutan antes del constructor
    
    public Persona(){
        System.out.println("Ejecucion del constructor");
    }
    
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
