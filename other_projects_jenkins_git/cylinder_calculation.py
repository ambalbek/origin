class Cylinder:
    
    x = int(input("enter height of the cylender:"))
       
    y = int(input("enter radius of the cylender:"))
        
    def __init__(self,height,radius):
        self.height= height
        self.radius = radius
    
        
    def volume(self):
        return 3.14*(self.radius**2)*self.height
    
    def surface_area(self):
        return (2*3.14*self.radius*self.height) +(2*3.14*self.radius**2)

    
    answer= Cylinder(x,y)
    print(answer.volume())
    print(answer.surface_area())
answer
