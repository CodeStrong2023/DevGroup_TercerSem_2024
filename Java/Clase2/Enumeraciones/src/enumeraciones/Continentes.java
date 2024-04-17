
package enumeraciones;

public enum Continentes {
    AFRICA(54, "1.216 miles de millones"),
    EUROPA(44, "746.4 millones"),
    ASIA(51, "4.753 miles de millones"),
    AMERICA(35, "662 millones "),
    OCEANIA(14, "43 millones ");
    
    
    private final int paises;
    private String habitantes;
    
    Continentes (int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;

    }

    //Método get
    public int getPaises() {
        return this.paises;
    }
    
    public String getHabitantes(){
        return this.habitantes;
    }
}

