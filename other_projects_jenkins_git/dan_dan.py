class A():
    def __init__(self,radius,length,width,height):
        self.radius = radius
        self.length = length
        self.width = width
        self.height= height
    def area(self):
        self.area1 = 4*(self.radius**2)*3.14
    def volume(self):
        self.volume1=(self.radius**3)*3.14*4/3
    def circumference(self):
        self.circumference1=2*3.14*self.radius
    def cube_volume(self):
        self.cube= self.length**3
    def cube_perimeter(self):
        self.cube_per= self.length*4
    def rectangle_volume(self):
        self.rectangle_vol= self.length*self.length*self.height
    def rectangle_perimeter(self):
        self.rectangle_per=2*(self.length+self.width)

while True:
    try:
        a=A(radius =int(input("please provide the Radius:")),length=int(input("please provide the length:")),width=int(input("please provide the width:")),height=int(input("please provide the height:")))
    except:
        print("are you dumb? please provide the number!")
        continue
    else:
        break


a.area()
a.volume()
a.circumference()
a.cube_volume()
a.cube_perimeter()
a.rectangle_volume()
a.rectangle_perimeter()
print(f'{a.area1:.1f}')
print(f'{a.volume1:.1f}')
print(f'{a.circumference1:.1f}')
print(a.cube_per)
print(a.cube)
print(a.rectangle_per)
print(a.rectangle_vol)