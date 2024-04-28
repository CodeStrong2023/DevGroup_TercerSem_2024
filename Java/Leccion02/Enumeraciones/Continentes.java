package Java.Leccion02.Enumeraciones;

public enum Continentes {
    AFRICA(54, "1.2 billones"),
    EUROPA(50, "746 millones"),
    ASIA(51, "4.5 billones"),
    AMERICA(35, "1 billon"),
    OCEANIA(14, "43 millones");

    private final int paises;
    private String habitantes;

    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }

    public int getPaises() {
        return this.paises;
    }

    public String getHabitantes() {
        return this.habitantes;
    }
    
}
