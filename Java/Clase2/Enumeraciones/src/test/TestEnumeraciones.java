
package test;


import enumeraciones.Continentes;
import enumeraciones.Dias;


public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: "+ Dias.LUNES);
        //indicarDiaSemana(Dias.VIERNES); //Las enumeraciones se tratan como cadenas, pero no se utilizan
        //comillas, se acceden atravez del operador de punto.
        System.out.println("Continente nº4: " + Continentes.AMERICA);
        System.out.println("nº de Países en el 4to Continente: " +Continentes.AMERICA.getPaises()) ;
        System.out.println("nº de Habitantes en el 4to Continente: " +Continentes.AMERICA.getHabitantes()) ;
        
        System.out.println("Continente nº1: " + Continentes.AFRICA);
        System.out.println("nº de Países en el 1er Continente: " +Continentes.AFRICA.getPaises()) ;
        System.out.println("nº de Habitantes en el 1er Continente: " +Continentes.AFRICA.getHabitantes()) ;
        
        System.out.println("Continente nº2: " + Continentes.EUROPA);
        System.out.println("nº de Países en el 4to Continente: " +Continentes.EUROPA.getPaises()) ;
        System.out.println("nº de Habitantes en el 4to Continente: " +Continentes.EUROPA.getHabitantes()) ;
        
        System.out.println("Continente nº3: " + Continentes.ASIA);
        System.out.println("nº de Países en el 4to Continente: " +Continentes.ASIA.getPaises()) ;
        System.out.println("nº de Habitantes en el 4to Continente: " +Continentes.ASIA.getHabitantes()) ;
        
        System.out.println("Continente nº5: " + Continentes.OCEANIA);
        System.out.println("nº de Países en el 5to Continente: " +Continentes.OCEANIA.getPaises()) ;
        System.out.println("nº de Habitantes en el 5to Continente: " +Continentes.OCEANIA.getHabitantes()) ;
        

        
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer día de la semana");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo día de la semana");
                break;
            default:
                System.out.println("Ese valor no correspondes");
            
        }
    }
}
