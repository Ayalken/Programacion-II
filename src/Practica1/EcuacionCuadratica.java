package Practica1;

public class EcuacionCuadratica {
    // Atributos privados
    private double a;
    private double b;
    private double c;

    // Constructor
    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    // Método para calcular el discriminante
    public double getDiscriminante() {
        return b * b - 4 * a * c;
    }

    // Método para calcular la primera raíz
    public double getRaiz1() {
        double disc = getDiscriminante();
        if (disc >= 0) {
            return (-b + Math.sqrt(disc)) / (2 * a);
        } else {
            return 0;
        }
    }

    // Método para calcular la segunda raíz
    public double getRaiz2() {
        double disc = getDiscriminante();
        if (disc >= 0) {
            return (-b - Math.sqrt(disc)) / (2 * a);
        } else {
            return 0;
        }
    }
}