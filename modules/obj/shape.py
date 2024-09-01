from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"I'm a shape named {self.name}, I'm a {type(self).__name__}"
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
        
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side