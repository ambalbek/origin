class Cube():
    def __init__(self, width,length, height):
        self.width = width
        self.length = length
        self.height = height
        
    def volume(self):
        return self.width*self.length*self.height
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return(2*(self.length+self.width))
    
    
a = (int(input("Enter length:")))
b= (int(input("enter width:")))
c=(int(input("enter height")))
total = Cube(a,b,c)
print('The volume of:',total.volume())
print('the area of:',total.area())
print('the perimeter of:',total.perimeter())
      