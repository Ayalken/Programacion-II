package Practica1;

import java.util.Scanner;

public class TestEcuacionCuadratica {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese a, b, c separados por espacio: ");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);

        double discriminante = ecuacion.getDiscriminante();

        if (discriminante > 0) {
            System.out.println("La ecuacion tiene dos raices: " 
                + ecuacion.getRaiz1() + " y " + ecuacion.getRaiz2());
        } else if (discriminante == 0) {
            System.out.println("La ecuacion tiene una raiz: " + ecuacion.getRaiz1());
        } else {
            System.out.println("La ecuacion no tiene raices reales");
        }

        sc.close();
    }
}