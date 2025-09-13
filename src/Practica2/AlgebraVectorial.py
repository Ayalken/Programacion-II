from multimethod import multimethod
import math

class AlgebraVectorial:
    def __init__(self,a,b):
        self.a=a
        self.b=b 
    #a)
    @multimethod
    def perpendicular(self):
        return (math.hypot(self.a[0]+self.b[0],self.a[1]+self.b[1]))==(math.hypot(self.a[0]-self.b[0],self.a[1]-self.b[1]))
    #b)
    @multimethod
    def perpendicular(self,flag_b:bool):
        return (math.hypot(self.a[0]-self.b[0], self.a[1]-self.b[1]))==(math.hypot(self.b[0]-self.a[0], self.b[1]-self.a[1]))
    #c)
    @multimethod
    def perpendicular(self,flag_c:int):
        return self.a[0]*self.b[0]+self.a[1]*self.b[1]==0
    #d)
    @multimethod
    def perpendicular(self,flag_d:float):
        return math.hypot(self.a[0]+self.b[0],self.a[1]+self.b[1])**2==math.hypot(self.a[0],self.a[1])**2 + math.hypot(self.b[0],self.b[1])**2
    #e)
    @multimethod
    def paralela(self):
        if self.b[0] !=0:
            r= self.a[0]/self.b[0]
            return r, self.a[1]==r*self.b[1]
        elif self.b[1] !=0:
            r=self.a[1]/self.b[1]
            return r, self.a[0]==r*self.b[0]
        else :
            return None ,self.a==(0,0)
    #f)
    @multimethod
    def paralela(self,flang_f:bool):
        return self.a[0]*self.b[1]-self.a[1]*self.b[0]==0
    #g)
    @multimethod
    def Proyeccion_de_a_sobre_b(self):
        return (
            ((self.a[0]*self.b[0]+self.a[1]*self.b[1]) / (self.b[0]**2+self.b[1]**2) *self.b[0]),
            ((self.a[0]*self.b[0]+self.a[1]*self.b[1]) / (self.b[0]**2+self.b[1]**2) *self.b[1])
        )
    #h)
    @multimethod
    def Componente_de_a_en_b(self,):
        return (
            ((self.a[0]*self.b[0]+self.a[1]*self.b[1])/(math.hypot(self.b[0],self.b[1])))
        )
        
        
        
a=(1,2)
b=(2,-1)
vectorN= AlgebraVectorial(a,b)
print("a) Perpendicular. Si el vector a es ortogonal o perpendicular a b:", vectorN.perpendicular())
print("b) Perpendicular. Si el vector a es mutuamente ortogonal a b",vectorN.perpendicular(True))
print("c) Perpendicular. Si el vector a es ortogonal a b:",vectorN.perpendicular(0))
print("d) Perpendicular. Si el vector a es ortogonal a b:",vectorN.perpendicular(0.0))
print("e) Paralela. Si el vector a es paralela a b:",vectorN.paralela())
print("f) Paralela. Si el vector a es paralela a b: ",vectorN.paralela(True))
print("g) Proyeccion de a sobre b. La proyecci´on ortogonal de a sobre b: Proyb",vectorN.Proyeccion_de_a_sobre_b())
print("h) Componente de a en b. El componente de a en la direcci´on de b: Compb",vectorN.Componente_de_a_en_b())