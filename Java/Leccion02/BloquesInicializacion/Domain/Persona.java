package Java.Leccion02.BloquesInicializacion.Domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;

    static{ // Bloque de inicializacion estático.
        System.out.println("Ejecucion del bloque estático.");
        ++Persona.contadorPersonas;
        // idPersona = 10; NO ES ESTATICO POR ESO NOS DA ERROR.
    }

    {// Bloque de inicializacion no estático o CONTEXTO DINAMICO
        System.out.println("Ejecucion del bloque NO estático.");
        this.idPersona = Persona.contadorPersonas++; // Incrementamos el atributo.
    }
    // Los bloques de inicializacion se ejecutan antes del constructor.

    public Persona(){
        System.out.println("Ejecucion del constructor.");
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona [idPersona=" + idPersona + "]";
    }
}
