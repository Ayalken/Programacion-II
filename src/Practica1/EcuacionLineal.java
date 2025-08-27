// Source code is decompiled from a .class file using FernFlower decompiler.
package Practica1;

public class EcuacionLineal {
   private double a;
   private double b;
   private double c;
   private double d;
   private double e;
   private double f;

   public EcuacionLineal(double var1, double var3, double var5, double var7, double var9, double var11) {
      this.a = var1;
      this.b = var3;
      this.c = var5;
      this.d = var7;
      this.e = var9;
      this.f = var11;
   }

   public boolean tieneSolucion() {
      return this.a * this.d - this.b * this.c != 0.0;
   }

   public double getX() {
      if (!this.tieneSolucion()) {
         throw new ArithmeticException("El sistema no tiene solución única.");
      } else {
         return (this.e * this.d - this.b * this.f) / (this.a * this.d - this.b * this.c);
      }
   }

   public double getY() {
      if (!this.tieneSolucion()) {
         throw new ArithmeticException("El sistema no tiene solución única.");
      } else {
         return (this.a * this.f - this.e * this.c) / (this.a * this.d - this.b * this.c);
      }
   }
}
