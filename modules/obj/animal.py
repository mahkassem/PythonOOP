from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"I'm an animal named {self.name}, I'm a {type(self).__name__}"
    
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def legs(self):
        pass
    
class Cat(Animal):
    def sound(self):
        print("Meow")
        
    def legs(self):
        print("Four legs")
        
    def _favorite_food(self):
        return self.__food()
    
    def __food(self):
        return "Milk"
        
class Dog(Animal):
    def sound(self):
        print("Bark")
        
    def legs(self):
        print("Four legs")
        
class StreetCat(Cat):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        print("Meooooooooow")
        
    def _favorite_food(self):
        return "Garbage"
