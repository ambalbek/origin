from math import pi


class Parameters:
    def __init__(self,length,width,height,radius,celcius,fahrenheit):
        self.length=length
        self.width=width
        self.height=height
        self.radius=radius
        self.celcius=celcius
        self.fahrenheit=fahrenheit
class Rectangle(Parameters):    
    def rectangle(self):
        a=self.length*self.width
        v=self.length*self.width*self.height
        p=(self.length+self.width)*2
        return "area of rectangle is %s"%a,"volume of rectangle is %s"%v,"perimeter of rectangle is %s"%p
class Circle(Rectangle):    
    def circle(self):
        a=pi*self.radius**2
        p=2*pi*self.radius
        return "area of circle is %.2f"%a,"perimeter of circle is %.2f"%p
class Cube(Circle):
    def cube(self):
        a=self.length**2
        v=self.length**3
        p=4*self.length
        return "area of square is %.2f"%a,"volume of cube is %.2f"%v, "perimeter of cube is %.2f"%p
class Temperature(Cube):    
    def temperature(self):
        fahrenheit1=(9/5*self.celcius)+32
        celcius1=(self.fahrenheit-32)*5/9
        return "degree in fahrenheit is %.2f"%fahrenheit1, "degree in celcius is %.2f"%celcius1
while True:
    try:
        temp=Temperature(length=float(input("plaese provide the length:")),width=float(input("plese provide the width:")),height=float(input("please provide the height:")),radius=float(input("please provide the radius:")),fahrenheit=int(input("please provide the temperature in fahrenheit:")),celcius=int(input("please provide the temperature in celcius:")))
    except:
        print("please provide the numbers!!!")
        continue
    else:
        break
print(temp.rectangle())
print(temp.circle())
print(temp.cube())
print(temp.temperature())
print(input())
       