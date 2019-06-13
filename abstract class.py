from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length =10
        self.breadth = 12

    def printarea(self):
        return self.length * self.breadth
    
gg= Rectangle()

print(gg.printarea())