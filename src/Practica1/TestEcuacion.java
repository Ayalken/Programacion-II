package Practica1;

import java.util.Scanner;
import java.util.Locale;

public class TestEcuacion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        while (true) {
            System.out.print("Ingrese a, b, c, d, e, f (o vacío para salir): ");
            String input = scanner.nextLine();
            if (input.trim().isEmpty()) break;

            input = input.replace(',', '.');

            try {
                String[] valores = input.trim().split("\\s+");
                if (valores.length != 6) {
                    System.out.println("Debe ingresar exactamente 6 números.");
                    continue;
                }

                double a = Double.parseDouble(valores[0]);
                double b = Double.parseDouble(valores[1]);
                double c = Double.parseDouble(valores[2]);
                double d = Double.parseDouble(valores[3]);
                double e = Double.parseDouble(valores[4]);
                double f = Double.parseDouble(valores[5]);

                EcuacionLineal ecuacion = new EcuacionLineal(a, b, c, d, e, f);

                if (ecuacion.tieneSolucion()) {
                    System.out.printf("x = %.1f, y = %.1f%n", ecuacion.getX(), ecuacion.getY());
                } else {
                    System.out.println("La ecuación no tiene solución");
                }

            } catch (NumberFormatException ex) {
                System.out.println("Error: ingrese solo números válidos.");
            }
        }

        scanner.close();
        System.out.println("Programa terminado.");
    }
}

//    9.0 4.0 3.0 -5.0 -6.0 -21.0
//    1.0 2.0 2.0 4.0 4.0 5.0