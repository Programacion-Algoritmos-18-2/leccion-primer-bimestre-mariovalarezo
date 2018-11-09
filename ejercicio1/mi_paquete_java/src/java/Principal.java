/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java;

import java.util.Scanner;

/**
 *
 * @author Mario
 */
public class Principal {
    /**
     * Metodo main
     * @param args 
     */
    public static void main(String[] args) {
        String n;
        double n1;
        Scanner leer = new Scanner(System.in);
        Empleado e = new Empleado("Luis","Benitez","110000001" ,0);
        System.out.println(e);
        System.out.println("Ingrese el nombre");
        n = leer.next();
        EmpleadoPorHora e2= new EmpleadoPorHora(n, "Andrade","11000001",0,20.2,15.0);
        System.out.println(e2);
        System.out.println("Ingrese la comision");
        n1= leer.nextDouble();
        EmpleadoFijo e3 = new EmpleadoFijo("Ana", "Diaz" ,"111000001",n1,3002.0,10.0);
        System.out.println(e3);
        EmpleadoPorSemana e4 = new EmpleadoPorSemana("Ana", "Andrade","11000001",0,20,15);
        System.out.println(e4); 
        
    }
    
}
