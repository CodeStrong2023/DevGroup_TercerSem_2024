
package test;

public class TestArguementosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3,4,5);
        imprimirNumeros(1,2);
        variosParametros("Gabriel", "Gonzalez", 19, 7, 8, 9);
    }
    
    private static void variosParametros(String nombre, String apellido, int edad, int ... numeros){
        System.out.println("Nombre: " + nombre+ " Apellido: " + apellido+ " Edad: " + edad);
        imprimirNumeros(numeros);
    }
    
    private static void imprimirNumeros(int ... numeros){
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: " + numeros[i]);
            
        }
    }
}
