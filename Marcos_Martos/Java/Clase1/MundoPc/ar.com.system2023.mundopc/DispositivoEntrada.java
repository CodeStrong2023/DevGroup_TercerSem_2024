package ar.com.system2023.mundopc;

public class DispositivoEntrada{
    private String tipoEntrada;
    private String marca;

    public DispositivoEntrada(String tipoEntrada, String marca){
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }

    public String getTipoEntrada(){
        return tipoEntrada;
    }

    public String setTipoEntrada(String tipoEntrada){
        this.tipoEntrada = tipoEntrada;
    }

    public String getMarca(){
        return marca;
    }

    public String setMarca(String marca){
        this.marca = marca;
    }

    @Override
    public String toString(){
        return "DispositivoEntrada{" + "tipoEntrada" + tipoEntrada + ", marca=" + marca + "}";
    }
}