
package domain;

public abstract class FiguraGeometrica {
    protected String tipoFigura;
    
    protected FiguraGeometrica(String tipoFigura){
        this.tipoFigura = tipoFigura;
    }
    
<<<<<<< HEAD
    //Metodo Abstracto
    public abstract void dibujar();
    
    //Agregamos el get y set 

    public String getTipoFigura() {
        return tipoFigura;
    }

    public void setTipoFigura(String tipoFigura) {
=======
    //Metodo abstracto
    public abstract void dibujar();
        
    //Agregamos el get y set
    
    public String getTipoFigura(){
        return tipoFigura;
    }
    public void setTipoFigura(){
>>>>>>> 7ed7ba0 (agregando ejercicios de Java, clase 5 videos 7 y 8)
        this.tipoFigura = tipoFigura;
    }

    @Override
    public String toString() {
        return "FiguraGeometrica{" + "tipoFigura=" + tipoFigura + '}';
<<<<<<< HEAD
    } 
    
}

=======
    }
    
    
}
>>>>>>> 7ed7ba0 (agregando ejercicios de Java, clase 5 videos 7 y 8)
