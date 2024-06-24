import java.util.Scanner;

public class CalculadoraUtn {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("****** Aplicación Calculadora ******");
        //Mostramos el menú
        System.out.println("""
                1. Suma
                2. Resta
                3. Multiplicación
                4. División
                5. Salir
                """);
        System.out.print("¿Operación a realizar?");
        var operacion = Integer.parseInt(entrada.nextLine());

        if (operacion >= 1 && operacion <= 4) {
            System.out.println("Digite el valor para el operando1: ");
            var operando1 = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite el valor para el operando2: ");
            var operando2 = Integer.parseInt(entrada.nextLine());

            int resultado;
            switch (operacion) {
                case 1 -> { //Suma
                    resultado = operando1 + operando2;
                    System.out.println("El resultado de la suma es: " + resultado);
                }
                case 2 -> { //Resta
                    resultado = operando1 - operando2;
                    System.out.println("El resultado de la resta es: " + resultado
                    );
                }
                case 3 -> { //Multiplicación
                    resultado = operando1 * operando2;
                    System.out.println("El resultado de la multiplicación es: " + resultado);
                }
                case 4 -> { //División
                    resultado = operando1 / operando2;
                    System.out.println("El resultado de la división es: " + resultado);
                }
                default -> System.out.println("Opción erronea: " + operacion);

            } //Fin switch

        } //Fin del if
        else if (operacion == 5) {
            System.out.println("Hasta pronto...");
        }
        else{
            System.out.println("Opción erronea: " + operacion);
        }

    } //Fin main

} //Fin clase