/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java;

/**
 *
 * @author Mario
 */
public class EmpleadoFijo extends Empleado {
    private double sueldo_fijo, des_seguro;
    /**
     * 
     * @param n nombre
     * @param a apellido
     * @param c
     * @param co
     * @param suf
     * @param suse 
     */
    public EmpleadoFijo(String n, String a, String c,double co, double suf , double suse){
        super(n,a,c,co);
        setsueldo_fijo(suf);
        setdes_seguro(suse);
        
    }
  
     public void setsueldo_fijo(double suf) {
        sueldo_fijo = suf;
    }

    public double getsueldo_fijo() {
        return sueldo_fijo;
    }
    
    
    
    public void setdes_seguro(double suse) {
        des_seguro = suse;
    }

    public double getdes_seguro() {
        return des_seguro;
    }
    
    public double calcular_suF(){
        double f =sueldo_fijo- des_seguro+comision_fija;
        
        return f;
        
    }
    
    
    @Override
    public String toString(){   
        return String.format("%s Sueldo Fijo %f Descuento Seguro %f Total %f", super.toString(), getsueldo_fijo(), getdes_seguro(), calcular_suF());
    }
    
}
