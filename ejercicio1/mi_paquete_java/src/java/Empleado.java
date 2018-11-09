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
public class Empleado {

    private String nombre, apellido, cedula;
    public double comision_fija;
/**
 * 
 * @param n nombre
 * @param a apellido
 * @param c cedula
 * @param co comision
 */
    public Empleado(String n, String a, String c, double co ) {
        setNombre(n);
        setApellido(a);
        setCedula(c);
        setcomision_fija(co);

    }
    
    //Metodos Get y set
    
    public void setcomision_fija(double n) {
        comision_fija = n;
    }

    public double getcomision_fija() {
        return comision_fija;
    }
    
    public void setNombre(String n) {
        nombre = n;
    }

    public String getNombre() {
        return nombre;
    }

    public void setApellido(String n) {
        apellido = n;
    }

    public String getApellido() {
        return apellido;
    }
    
     public void setCedula(String c) {
        cedula = c;
    }

    public String getCedula() {
        return cedula;
    }
  /**
   * Overrride 
   * @return 
   */  
    @Override
    public String toString(){
        return String.format("Informacion de:\n%s %s\nCedula %s", 
                getNombre(), getApellido(), getCedula());
    }

}
