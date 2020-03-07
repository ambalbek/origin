from math import pi
'''
this is  my class inheritance example
'''
#first I should create super-class and I will call it A===> keep in your mind class name should be capitalized!!!
class A:
    #initial function usually calls __init__(and some atributes inside)
    def __init__(self, length,width,height,radius):
        #rename your atributes adding self. on it
        self.length=length
        self.width=width
        self.height=height
        self.radius=radius
    def surface(self):
        cube=6*self.length**2
        sphere=4*(pi*self.radius**2)
        return "serface of cube is: %s"%cube,"surface of sphere is: %.2f"%sphere
    def area(self):
        cube=self.length**2
        circle=(self.radius**2)*pi
        return "area of cube is: %s"%cube,"area of circle is:%.2f"%circle
class B(A):
    #this is your child class I will call it B
    def volumes(self):
        cube=self.length**3
        sphere=4/3*(pi*self.radius**3)        
        return "volume of cube is:%s"%cube,"volume of sphere is:%.2f"%sphere
    def circumference(self):
        circumference=2*pi*self.radius
        return "circumference of sphere is:%.2f"%circumference
class C(B):
    # and this will be your grandchild class and I will call it C
    def perimeter(self):
        rectangle=2*(self.length+self.width)
        cube=4*self.length
        circle=2*pi*self.radius
        return "perimeter of rectangle is:%s"%rectangle,"perimeter of cube is:%s"%cube,"perimeter of circle is:%.2f"%circle
#commands to get some results
a=C(5,3,2,7)
print(a.surface())
print(a.area())
print(a.volumes())
print(a.circumference())
print(a.perimeter())
'''
as you see in my result you should call grandchild!
cuz when you call grandchild it will call the parents:)
'''