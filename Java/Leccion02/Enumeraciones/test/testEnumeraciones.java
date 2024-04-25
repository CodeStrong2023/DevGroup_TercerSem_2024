package Java.Leccion02.Enumeraciones.test;

import Java.Leccion02.Enumeraciones.Continentes;
import Java.Leccion02.Enumeraciones.Dias;

public class testEnumeraciones {
    public static void main(String[] args) {
        // System.out.println("\nDia 1: " + Dias.LUNES);
        // indicarDiaSemana(Dias.DOMINGO);
        System.out.println("\nContinente No. 1: " + Continentes.AFRICA);
        System.out.println("No. de paises: " + Continentes.AFRICA.getPaises());
        System.out.println("No. de habitantes: " + Continentes.AFRICA.getHabitantes());
        System.out.println("\nContinente No. 2: " + Continentes.EUROPA);
        System.out.println("No. de paises: " + Continentes.EUROPA.getPaises());
        System.out.println("No. de habitantes: " + Continentes.EUROPA.getHabitantes());
        System.out.println("\nContinente No. 3: " + Continentes.ASIA);
        System.out.println("No. de paises: " + Continentes.ASIA.getPaises());
        System.out.println("No. de habitantes: " + Continentes.ASIA.getHabitantes());
        System.out.println("\nContinente No. 4: " + Continentes.AMERICA);
        System.out.println("No. de paises: " + Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes: " + Continentes.AMERICA.getHabitantes());
        System.out.println("\nContinente No. 5: " + Continentes.OCEANIA);
        System.out.println("No. de paises: " + Continentes.OCEANIA.getPaises());
        System.out.println("No. de habitantes: " + Continentes.OCEANIA.getHabitantes());
    }

    private static void indicarDiaSemana (Dias dias){
        switch (dias) {
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana:");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;
            default:
                System.out.println("Dia de la semana inexistente");
                break;
        }
    }
}
