import TerSem2024Local.Java.Leccion03.ForEach.domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9}; // Sintaxis resumida
        for (int edad: edades) { // Sintaxis ForEach
            System.out.println("Edad: " + edad);
        }
        Persona personas[] = {new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};

        // for each
        for(Persona persona: personas){
            System.out.println("Persona = " + persona);
        }
    }
}
