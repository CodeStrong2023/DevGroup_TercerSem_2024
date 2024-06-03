<<<<<<< HEAD
package domain;

public class Rectangulo extends FiguraGeometrica {
    //constructor
    
    public Rectangulo(String tipoFigura){
        super(tipoFigura);
    }
    
    @Override
    public void dibujar(){ //implementando un metodo
        System.out.println("Se imprime un: "+this.getClass().getSimpleName());
    }
=======

package domain;

public class Rectangulo extends FiguraGeometrica{

    //Constructor
    public Rectangulo(String tipoFigura){
        super(tipoFigura); 
    }
    @Override
    public void dibujar(){ //Implementando el metodo
        System.out.println("Se imprime un: " + this.getClass().getSimpleName());
    }
           
    
>>>>>>> 7ed7ba0 (agregando ejercicios de Java, clase 5 videos 7 y 8)
}
