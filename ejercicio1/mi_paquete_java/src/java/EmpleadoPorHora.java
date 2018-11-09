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
public class EmpleadoPorHora extends Empleado {
    private double numero_hora, valor_hora;
    public EmpleadoPorHora(String n, String a, String c,double co, double nuh , double vah){
        super(n,a,c,co);
        setnumero_hora( nuh);
        setvalor_hora(vah);
          
    }
     public void setnumero_hora(double suf) {
        numero_hora = suf;
    }

    public double getumero_hora() {
        return numero_hora;
    }
    
    public void setvalor_hora(double suf) {
        valor_hora = suf;
    }

    public double getvalor_hora() {
        return valor_hora;
    }
    
    public double calcular_suF(){
        double f =numero_hora* valor_hora;        
        return f;
        
    }
    
    
    @Override
    public String toString(){   
        return String.format("%s Numero de horas %f Valor por hora %f Total %f", super.toString(), getumero_hora(), getvalor_hora(), calcular_suF());
    }
    
}
