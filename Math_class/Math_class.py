class Math:
    
    pi = 3.14
    
    class Circle:
        def __init__(self,diameter):
            self.radius = diameter/2
        def area(self):
            self.area = pi * self.radius ** 2
            return (self.area)
        def circumference(self):
            self.perimeter = 2 * pi * self.radius


            
    class Triangle:
        def __init__(self,base,height,angle1,angle2,angle3):
            self.base = base
            self.height = height
            self.angle1 = angle1
            self.angle2 = angle2
            self.angle3 = angle3
        def area(self):
            self.area = self.base * self.height
            return (self.area)
        def perimeter(self):
            self.perimeter = self.angle1 + self.angle2 + self.angle3

            
    class Rectangle:
        def __init__(self,width,height):
            self.width = width
            self.height = height
        def area(self):
            self.area = self.width * self.height
            return (self.area)
        def perimeter(self):
            self.perimeter = 2(self.width) + 2(self.height)


            
    class Square:
        def __init__(self,side_length):
            self.side_length = side_length
            
        def area(self):
            self.area = self.side_length **2
            return (self.area)
        def perimeter(self):
            self.perimeter = self.side_length * 4

    class Parallelogram:
        def __init__(self,base,height):
            self.base = base
            self.height = height
        def area(self):
            self.area = self.height * self.base * .5
            return (self.area)
        def perimeter(self):
            self.perimeter = 2(self.base + self.height)

    class Sphere:
        def __init__(self,diameter):
            self.radius = diameter/2
        def area(self):
            self.area = 4 * Math.pi * (self.radius **2)
            return (self.area)
        def volume(self):
            self.volume = (4/3) * pi * (self.radius **3)





