import math

class VectorTridimensional:
    def __init__(self, a: float, b: float, c: float):
        self.a=a
        self.b=b
        self.c=c

    # a)
    def __add__(self, o):
        return VectorTridimensional(self.a+o.a,
                                    self.b + o.b,
                                    self.c + o.c)
    # b)
    def __mul__(self, e: float):
        return VectorTridimensional(self.a * e,
                                    self.b * e,
                                    self.c * e)
    __rmul__ = __mul__
    # c)
    def __abs__(self):
        return math.sqrt(self.a**2 + self.b**2 + self.c**2)
    # d) 
    def normal(self):
        length = math.sqrt(self.a**2 + self.b**2 + self.c**2)
        if length == 0:
            raise ValueError("No se puede normalizar un vector nulo.")
        return VectorTridimensional(self.a/length,
                                self.b/length,
                                self.c/length)
    # e)
    def dot(self, o):
        return self.a*o.a + self.b*o.b + self.c*o.c
    # f)
    def cross(self, o):
        return VectorTridimensional(self.b*o.c - self.c*o.b,
                                    self.c*o.a - self.a*o.c,
                                    self.a*o.b - self.b*o.a)
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
a = VectorTridimensional(1, 2, 3)
b = VectorTridimensional(4, -1, 2)

print("a)Suma de dos vectores a y b: c =a+b=  ", a + b)
print("b)Multiplicacion de un escalar r por un vector a: b=ra=  ", 2 * a)
print("c)Longitud de un vector a: |a|=  ", abs(a))
print("d)Normal de un vector a: b=a/|a|=  ", a.normal())
print("e)Producto escalar de a y b: a·b=  ", a.dot(b))
print("f)Producto vectorial de a y b:a×b=  ", a.cross(b)) 
if a.dot(b) == 0:
    print("a y b son perpendiculares.")
else:
    print("a y b NO son perpendiculares.")
